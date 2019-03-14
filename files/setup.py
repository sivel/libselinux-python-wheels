#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


setup(
    name='libselinux-python',
    version=os.getenv('VERSION', None),
    description='SELinux python bindings for libselinux',
    long_description='The libselinux-python package contains the python '
                     'bindings for developing SELinux applications.',
    url='https://github.com/SELinuxProject/selinux/wiki',
    packages=['selinux'],
    package_dir={'selinux': 'selinux'},
    package_data={'selinux': ['selinux/*.so']},
    include_package_data=True,
    license='Public Domain',
)
