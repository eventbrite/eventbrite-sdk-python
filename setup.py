#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = ["requests",]

test_requirements = []

# Add Python 2.6-specific dependencies
if sys.version_info[:2] < (2, 7):
    requirements.append('simplejson')
    test_requirements.append('unittest2')

# Add Python 2.7-specific dependencies
if sys.version < '3':
    test_requirements.append('mock')

setup(
    name='eventbrite',
    version='3.0.0',
    description='Official Eventbrite SDK for Python',
    long_description=readme + '\n\n' + history,
    author='Daniel Greenfeld',
    author_email='danny@eventbrite.com',
    url='https://github.com/pydanny/eventbrite',
    packages=[
        'eventbrite',
    ],
    package_dir={'eventbrite':
                 'eventbrite'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='eventbrite',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
