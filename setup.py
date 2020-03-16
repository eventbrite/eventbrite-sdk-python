#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '3.3.5'

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'test':
    os.system('pytest')
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()
with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

install_requires = [
    "requests>=2.0",
]

tests_require = [
    'coverage',
    'flake8',
    'mock; python_version < "3"',
    'pytest',

]

setup(
    name='eventbrite',
    version=__version__,
    description='Official Eventbrite SDK for Python',
    long_description=readme + '\n\n' + history,
    author='Daniel Greenfeld, Bartek Ogryczak',
    author_email='danny@eventbrite.com',
    url='https://github.com/eventbrite/eventbrite-sdk-python',
    packages=[
        'eventbrite',
    ],
    package_dir={
        'eventbrite': 'eventbrite',
    },
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'testing': tests_require,
    },
    license="Apache",
    zip_safe=False,
    keywords='eventbrite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    test_suite='tests'
)
