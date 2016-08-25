#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_requires = [
    'bigchaindb_driver>=0.0.3',
]

tests_require = [
    'coverage',
    'pep8',
    'pyflakes',
    'pylint',
    'pytest-cov',
]

dev_require = [
    'ipdb',
    'ipython',
]

docs_require = [
    'Sphinx>=1.3.5',
    'sphinx-autobuild',
    'sphinxcontrib-napoleon>=0.4.4',
    'sphinx_rtd_theme',
]

dependency_links = [
    'git+https://github.com/bigchaindb/bigchaindb-driver.git#egg=bigchaindb_driver-0.0.3',
]

setup(
    name='coalaip-bigchaindb',
    version='0.0.1.dev1',
    description="BigchainDB ledger plugin for COALA IP's Python reference implementation",
    long_description=readme + '\n\n' + history,
    author="BigchainDB",
    author_email='dev@bigchaindb.com',
    url='https://github.com/bigchaindb/pycoalaip-bigchaindb',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'dev': dev_require + tests_require + docs_require,
        'docs': docs_require,
    },
    test_suite='tests',
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=['coalaip', 'coalaip plugin', 'bigchaindb'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    dependency_links=dependency_links,
)
