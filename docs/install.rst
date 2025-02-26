..  _install:

Installation
************

ReproZip is available as open source, released under the Revised BSD License. The tool is comprised of two components: **reprozip** (for the packing step) and **reprounzip** (for the unpack step). Additional components and plugins are also provided for *reprounzip*: **reprounzip-vagrant**, which unpacks the experiment in a Vagrant virtual machine; **reprounzip-docker**, which unpacks the experiment in a Docker container; and **reprounzip-vistrails**, which creates a VisTrails workflow to reproduce the experiment. More plugins may be developed in the future (and, of course, you are free to :ref:`roll your own <develop-plugins>`).
In our `website <https://www.reprozip.org/>`__, you can find links to our PyPI packages and our `GitHub repository <https://github.com/ViDA-NYU/reprozip>`__.

In the following, you will find installation instructions for :ref:`linux`, :ref:`mac`, and :ref:`windows`. ReproZip is also available for the :ref:`conda` Python distribution.

..  _linux:

Linux
=====

For Linux distributions, both *reprozip* and *reprounzip* components are available.

Required Software Packages
--------------------------

Python 2.7.3 or greater, or 3.3 or greater is required to run ReproZip [#bug]_. If you don't have Python on your machine, you can get it from `python.org <https://www.python.org/>`__. You will also need the `pip <https://pip.pypa.io/en/latest/installing/>`__ installer.

Besides Python and pip, each component or plugin to be used may have additional dependencies that you need to install (if you do not have them already installed in your environment), as described below:

+------------------------+-------------------------------------------------+
| Component / Plugin     | Required Software Packages                      |
+========================+=================================================+
| *reprozip*             | `SQLite <https://www.sqlite.org/>`__,           |
|                        | Python headers,                                 |
|                        | a working C compiler                            |
+------------------------+-------------------------------------------------+
| *reprounzip*           | None                                            |
+------------------------+-------------------------------------------------+
| *reprounzip-vagrant*   | Python headers,                                 |
|                        | a working C compiler,                           |
|                        | `Vagrant v1.1+ <https://www.vagrantup.com/>`__, |
|                        | `VirtualBox <https://www.virtualbox.org/>`__    |
+------------------------+-------------------------------------------------+
| *reprounzip-docker*    | `Docker <https://www.docker.com/>`__            |
+------------------------+-------------------------------------------------+
| *reprounzip-vistrails* | None [#vis1]_                                   |
+------------------------+-------------------------------------------------+

Debian and Ubuntu
`````````````````

You can get all the required dependencies using APT::

    apt-get install python python-dev python-pip gcc libsqlite3-dev libssl-dev libffi-dev

Fedora & CentOS
```````````````

You can get the dependencies using the Yum packaging manager::

    yum install python python-devel gcc sqlite-devel openssl-devel libffi-devel

..  [#bug] ``reprozip`` and ``reprounzip graph`` will not work before 2.7.3 due to `Python bug 13676 <https://bugs.python.org/issue13676>`__ related to sqlite3. Python 2.6 is ancient and unsupported.
..  [#vis1] `VisTrails v2.2.3+ <https://www.vistrails.org/>`__ is required to run the workflow generated by the plugin.

Installing *reprozip*
---------------------

To install or update the *reprozip* component, simply run the following command::

    $ pip install -U reprozip

Installing *reprounzip*
-----------------------

You can install or update *reprounzip* with all the available components and plugins using::

    $ pip install -U reprounzip[all]

Or you can install *reprounzip* and choose components manually::

    # Example, this installs all the components
    $ pip install -U reprounzip reprounzip-docker reprounzip-vagrant reprounzip-vistrails

..  _mac:

Mac OS X
========

For Mac OS X, only the *reprounzip* component is available.

Binaries
--------

An installer containing Python 2.7, *reprounzip*, and all the plugins can be `downloaded from GitHub <http://reprozip-files.s3-website-us-east-1.amazonaws.com/mac-installer>`__.

Required Software Packages
--------------------------

Python 2.7.3 or greater, or 3.3 or greater is required to run ReproZip [#bug2]_. If you don't have Python on your machine, you can get it from `python.org <https://www.python.org/>`__; you should prefer a 2.x release to a 3.x one. You will also need the `pip <https://pip.pypa.io/en/latest/installing/>`__ installer.

Besides Python and pip, each component or plugin to be used may have additional dependencies that you need to install (if you do not have them already installed in your environment), as described below:

+------------------------+-------------------------------------------------+
| Component / Plugin     | Required Software Packages                      |
+========================+=================================================+
| *reprounzip*           | None                                            |
+------------------------+-------------------------------------------------+
| *reprounzip-vagrant*   | Python headers,                                 |
|                        | `Vagrant v1.1+ <https://www.vagrantup.com/>`__, |
|                        | `VirtualBox <https://www.virtualbox.org/>`__    |
+------------------------+-------------------------------------------------+
| *reprounzip-docker*    | `Docker <https://www.docker.com/>`__            |
+------------------------+-------------------------------------------------+
| *reprounzip-vistrails* | None [#vis2]_                                   |
+------------------------+-------------------------------------------------+

You will need Xcode installed, which you can get from the Mac App Store, and the Command Line Developer Tools; instrucions on installing the latter may depend on your Mac OS X version (some information on StackOverflow `here <https://stackoverflow.com/questions/9329243/how-to-install-xcode-command-line-tools/9329325#9329325>`__).

..  seealso:: :ref:`Why does reprounzip-vagrant installation fail with error "unknown argument: -mno-fused-madd" on Mac OS X? <compiler_mac>`

..  [#bug2] ``reprozip`` and ``reprounzip graph`` will not work before 2.7.3 due to `Python bug 13676 <https://bugs.python.org/issue13676>`__ related to sqlite3. Python 2.6 is ancient and unsupported.
..  [#vis2] `VisTrails v2.2.3+ <https://www.vistrails.org/>`__ is required to run the workflow generated by the plugin.

Installing *reprounzip*
-----------------------

First, be sure to upgrade `setuptools`::

    $ pip install -U setuptools

You can install or update *reprounzip* with all the available components and plugins using::

    $ pip install -U reprounzip[all]

Or you can install *reprounzip* and choose components manually::

    # Example, this installs all the components
    $ pip install -U reprounzip reprounzip-docker reprounzip-vagrant reprounzip-vistrails

..  _windows:

Windows
=======

For Windows, only the *reprounzip* component is available.

Binaries
--------

A 32-bit installer containing Python 2.7, *reprounzip*, and all the plugins can be `downloaded from GitHub <http://reprozip-files.s3-website-us-east-1.amazonaws.com/windows-installer>`__.

Required Software Packages
--------------------------

Python 2.7.3 or greater, or 3.3 or greater is required to run ReproZip [#bug3]_. If you don't have Python on your machine, you can get it from `python.org <https://www.python.org/>`__; you should prefer a 2.x release to a 3.x one. You will also need the `pip <https://pip.pypa.io/en/latest/installing/>`__ installer.

Besides Python and pip, each component or plugin to be used may have additional dependencies that you need to install (if you do not have them already installed in your environment), as described below:

+------------------------+------------------------------------------------------------------------+
| Component / Plugin     | Required Software Packages                                             |
+========================+========================================================================+
| *reprounzip*           | None                                                                   |
+------------------------+------------------------------------------------------------------------+
| *reprounzip-vagrant*   | `Vagrant v1.1+ <https://www.vagrantup.com/>`__,                        |
|                        | `VirtualBox <https://www.virtualbox.org/>`__                           |
+------------------------+------------------------------------------------------------------------+
| *reprounzip-docker*    | `Docker <https://www.docker.com/>`__ [#windowshome]_                   |
+------------------------+------------------------------------------------------------------------+
| *reprounzip-vistrails* | None [#vis3]_                                                          |
+------------------------+------------------------------------------------------------------------+

..  [#bug3] ``reprozip`` and ``reprounzip graph`` will not work before 2.7.3 due to `Python bug 13676 <https://bugs.python.org/issue13676>`__ related to sqlite3. Python 2.6 is ancient and unsupported.
..  [#vis3] `VisTrails v2.2.3+ <https://www.vistrails.org/>`__ is required to run the workflow generated by the plugin.
..  [#windowshome] Windows Professional Edition is required for Docker, it will not work on Windows Home Edition; `see FAQ <https://docs.docker.com/desktop/faqs/#can-i-install-docker-desktop-on-windows-10-home>`__.

Installing *reprounzip*
-----------------------

You can install or update *reprounzip* with all the available components and plugins using::

    $ pip install -U reprounzip[all]

Or you can install *reprounzip* and choose components manually::

    # Example, this installs all the components
    $ pip install -U reprounzip reprounzip-docker reprounzip-vagrant reprounzip-vistrails

..  _conda:

Anaconda
========

*reprozip* and *reprounzip* can also be installed on the `Anaconda <https://www.anaconda.com/products/individual#Downloads>`__ Python distribution, from anaconda.org::

    $ conda install --channel conda-forge reprozip reprounzip reprounzip-docker reprounzip-vagrant reprounzip-vistrails

Note, however, that *reprozip* is only available for Linux.
