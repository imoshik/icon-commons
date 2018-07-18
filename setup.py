#!/usr/bin/env python
import os

from setuptools import setup, find_packages

requires = [
    "coloredlogs"
]

with open(os.path.join('.', 'VERSION')) as version_file:
    version = version_file.read().strip()

setup_options = {
    'name': 'iconCommon',
    'version': version,
    'description': 'icon commmon package for python',
    'author': 'ICON foundation',
    'packages': find_packages(exclude=['tests*', 'docs']),
    'license': "Apache License 2.0",
    'install_requires': requires,
    'setup_requires': ['pytest-runner'],
    'tests_requires': ['pytest'],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ]
}

setup(**setup_options)