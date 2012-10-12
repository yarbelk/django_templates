#!/usr/bin/env python
"""
=============================================================================
django-{{project_name}}
=============================================================================

django-{{ project_name }} is a django application for doing things with Magic
Ponies"""

from setuptools import setup, find_packages

setup(
    name='django-{{ project_name }}',
    version='0.1',
    author='Your Name',
    author_email='your@email',
    url='www.your.url',
    description='Django-{{ project_name }} is an app for doing things with Magic Poneis',
    long_description=__doc__,
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    install_requires=[
        'requests==0.14.0'
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={},
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django'
    ],
)
