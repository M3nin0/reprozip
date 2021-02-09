import logging
import requests
import time

from reprounzip.parameters import _bundled_parameters
from reprounzip.utils import itervalues


logger = logging.getLogger(__name__)


def _vagrant_req(method, url, json):
    headers = {'User-Agent': 'reprozip testsuite'}
    if json:
        headers['Accept'] = 'application/json'
    for _ in range(5):
        res = requests.request(
            method,
            url,
            headers=headers,
            allow_redirects=True,
        )
        if res.status_code == 429:
            logger.info("(got 429, sleeping)")
            time.sleep(60)
        else:
            return res


def check_vagrant():
    error = False

    # Get all Vagrant boxes from bundled parameters
    boxes = set()
    for distribution in itervalues(
        _bundled_parameters['vagrant_boxes']['boxes'],
    ):
        for version in distribution['versions']:
            for image in itervalues(version['architectures']):
                boxes.add(image)

    # Check that they exist
    for box in boxes:
        # Get metadata
        url = 'https://vagrantcloud.com/' + box
        metadata = _vagrant_req(
            'GET',
            url,
            True,
        )
        if metadata.status_code != 200:
            logger.error(
                "Vagrant box not found: %d %s",
                metadata.status_code, url,
            )
            error = True
            continue
        metadata = metadata.json()

        # Find most recent version
        versions = [
            v for v in metadata.get('versions', ())
            if v.get('status') == 'active'
        ]
        if not versions:
            logger.error("No versions for Vagrant box %s", box)
            error = True
            continue
        max_version = max(metadata['versions'], key=lambda v: v['version'])

        # Go over each provider
        for provider in max_version['providers']:
            url = provider['url']
            res = _vagrant_req(
                'HEAD',
                url,
                False,
            )
            # Status should be 200
            if res.status_code != 200:
                logger.error(
                    "Got %d getting Vagrant box %s: %s",
                    res.status_code, box, url,
                )
                error = True
            # Content-Type should not start with "text/" (but can be unset)
            elif res.headers.get('Content-Type', '').startswith('text/'):
                logger.error(
                    "Got type %s getting Vagrant box %s: %s",
                    res.headers['Content-Type'], box, url,
                )
                error = True
            # Size should be at least 10 MB
            elif int(res.headers.get('Content-Length', 1E8)) < 1E7:
                logger.error(
                    "Got file size %s getting Vagrant box %s: %s",
                    res.headers['Content-Length'], box, url,
                )
                error = True
            else:
                logger.info("Vagrant box ok: %s (%s)", box, provider['name'])

    if error:
        raise AssertionError("Missing Vagrant boxes")


def check_docker():
    pass