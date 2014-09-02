# Copyright (C) 2014 New York University
# This file is part of ReproZip which is released under the Revised BSD License
# See file LICENSE for full license details.

"""Entry point for the reprounzip utility.

This contains :func:`~reprounzip.reprounzip.main`, which is the entry point
declared to setuptools. It is also callable directly.

It dispatchs to plugins registered through pkg_resources as entry point
``reprounzip.unpackers``.
"""

from __future__ import absolute_import, unicode_literals

import logging
import platform
from rpaths import Path
import tarfile

from reprounzip.unpackers.common import load_config, COMPAT_OK, COMPAT_MAYBE, \
    COMPAT_NO
from reprounzip.utils import iteritems, hsize


def print_info(args, unpackers):
    """Writes out some information about a pack file.
    """
    pack = Path(args.pack[0])

    # Loads config
    runs, packages, other_files = config = load_config(pack)

    pack_total_size = 0
    pack_total_paths = 0
    pack_files = 0
    pack_dirs = 0
    pack_symlinks = 0
    pack_others = 0
    tar = tarfile.open(str(pack), 'r:*')
    for m in tar.getmembers():
        if not m.name.startswith('DATA/'):
            continue
        pack_total_size += m.size
        pack_total_paths += 1
        if m.isfile():
            pack_files += 1
        elif m.isdir():
            pack_dirs += 1
        elif m.issym():
            pack_symlinks += 1
        else:
            pack_others += 1
    tar.close()

    meta_total_paths = 0
    meta_packed_packages_files = 0
    meta_unpacked_packages_files = 0
    meta_packages = len(packages)
    meta_packed_packages = 0
    for package in packages:
        nb = len(package.files)
        meta_total_paths += nb
        if package.packfiles:
            meta_packed_packages_files += nb
            meta_packed_packages += 1
        else:
            meta_unpacked_packages_files += nb
    nb = len(other_files)
    meta_total_paths += nb
    meta_packed_paths = meta_packed_packages_files + nb

    if runs:
        meta_architecture = runs[0]['architecture']
        if any(r['architecture'] != meta_architecture
               for r in runs):
            logging.warning("Runs have different architectures")
        meta_distribution = runs[0]['distribution']
        if any(r['distribution'] != meta_distribution
               for r in runs):
            logging.warning("Runs have different distributions")

    current_architecture = platform.machine().lower()
    current_distribution = platform.linux_distribution()[0:2]

    print("Pack file: %s" % pack)
    print("----- Pack information -----")
    print("Compressed size: %s" % hsize(pack.size()))
    print("Unpacked size: %s" % hsize(pack_total_size))
    print("Total packed paths: %d" % pack_total_paths)
    print("    Files: %d" % pack_files)
    print("    Directories: %d" % pack_dirs)
    print("    Symbolic links: %d" % pack_symlinks)
    if pack_others:
        print("    Unknown (what!?): %d" % pack_others)
    print("----- Metadata -----")
    print("Total paths: %d" % meta_total_paths)
    print("Listed packed paths: %d" % meta_packed_paths)
    if packages:
        print("Total software packages: %d" % meta_packages)
        print("Packed software packages: %d" % meta_packed_packages)
        print("    Files from packed software packages: %d" %
              meta_packed_packages_files)
        print("    Files from unpacked software packages: %d" %
              meta_unpacked_packages_files)
    if runs:
        print("Architecture: %s (current: %s)" % (meta_architecture,
                                                  current_architecture))
        print("Distribution: %s (current: %s)" % (
              meta_distribution, current_distribution or "(not Linux)"))
        print("Executions (%d):" % len(runs))
        for r in runs:
            print("    %s" % ' '.join(r['argv']))
            print("        input files: %s" % (", ".join(r['input_files'])))
            print("        output files: %s" % (", ".join(r['output_files'])))
            print("        wd: %s" % r['workingdir'])
            if 'signal' in r:
                print("        signal: %d" % r['signal'])
            else:
                print("        exitcode: %d" % r['exitcode'])

    # Unpacker compatibility
    print("----- Unpackers -----")
    unpacker_status = {}
    for name, upk in iteritems(unpackers):
        if 'test_compatibility' in upk:
            compat = upk['test_compatibility']
            if callable(compat):
                compat = compat(pack, config=config)
            if isinstance(compat, (tuple, list)):
                compat, msg = compat
            else:
                msg = None
            unpacker_status.setdefault(compat, []).append((name, msg))
        else:
            unpacker_status.setdefault(None, []).append((name, None))
    for s, n in [(COMPAT_OK, "Compatible"), (COMPAT_MAYBE, "Unknown"),
                 (COMPAT_NO, "Incompatible")]:
        if s not in unpacker_status:
            continue
        upks = unpacker_status[s]
        print("%s (%d):" % (n, len(upks)))
        for upk_name, msg in upks:
            if msg is not None:
                print("    %s (%s)" % (upk_name, msg))
            else:
                print("    %s" % upk_name)