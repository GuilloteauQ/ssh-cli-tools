#! /usr/bin/env python
# -*- coding:utf-8 -*-

# This file is a part of IoT-LAB ssh-cli-tools
# Copyright (C) 2015 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

"""SSH-CLI-Tools setuptools script."""

import os
from setuptools import setup, find_packages

PACKAGE = 'iotlabsshcli'
# GPL compatible http://www.gnu.org/licenses/license-list.html#CeCILL
LICENSE = 'CeCILL v2.1'


def readme(fname):
    """Utility function to read the README. Used for long description."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version(package):
    """ Extract package version without importing file
    Importing cause issues with coverage,
        (modules can be removed from sys.modules to prevent this)
    Importing __init__.py triggers importing rest and then requests too

    Inspired from pep8 setup.py
    """
    version = '-1'
    with open(os.path.join(package, '__init__.py')) as init_fd:
        for line in init_fd:
            if line.startswith('__version__'):
                version = eval(line.split('=')[-1])  # pylint:disable=eval-used
                break
    return version


SCRIPTS = ['iotlab-ssh']
DEPRECATED_SCRIPTS = ['open-a8-cli']

SCRIPTS += DEPRECATED_SCRIPTS

INSTALL_REQUIRES = ['iotlabcli>=2.0', 'parallel-ssh>=2.5.4',
                    'scp', 'gevent>=1.1', 'psutil']

setup(
    name=PACKAGE,
    version=get_version(PACKAGE),
    description='IoT-LAB testbed ssh command-line client',
    long_description=readme('README.rst'),
    long_description_content_type='text/x-rst',
    author='IoT-LAB Team',
    author_email='admin@iot-lab.info',
    url='http://www.iot-lab.info',
    license=LICENSE,
    download_url='http://github.com/iot-lab/ssh-cli-tools/',
    packages=find_packages(),
    scripts=SCRIPTS,
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Intended Audience :: End Users/Desktop',
                 'Environment :: Console',
                 'Topic :: Utilities', ],
    install_requires=INSTALL_REQUIRES,
)
