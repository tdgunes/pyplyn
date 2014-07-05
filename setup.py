#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyplyn

from distutils.core import setup

setup(
    name="pyplyn",
    version=pyplyn.__version__,
    author='Taha Dogan Gunes',
    author_email='tdgunes@gmail.com',
    url='https://github.com/tdgunes/pyplyn',
    packages=['pyplyn',],
    license='MIT',
    long_description=open('README.rst').read(),
)