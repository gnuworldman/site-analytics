#!/usr/bin/env python
"""Setup for the site_analytics project"""

import os

from setuptools import find_packages, setup


THIS_DIRECTORY = os.path.dirname(__file__)

def read_file(path):
    return open(os.path.join(THIS_DIRECTORY, path)).read()

# Set __version_info__ and __version__ from the _version.py module code.
exec(read_file(os.path.join('src', 'site_analytics', '_version.py')))

requires = read_file(os.path.join('requirements', 'run.txt')).splitlines()

setup(
    name='site_analytics',
    version=__version__,
    author="Craig Hurd-Rindy",
    author_email="gnuworldman@gmail.com",
    maintainer="Craig Hurd-Rindy",
    maintainer_email="gnuworldman@gmail.com",
    url='https://github.com/gnuworldman/site_analytics',
    description="Site Analytics REST service",
    long_description=read_file('README.rst'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=requires,
)
