# -*- coding: utf-8 -*-
from setuptools import setup

try:
    import multiprocessing
except ImportError:
    pass

setup(
    setup_requires=['pbr'],
    pbr=True,
    test_suite='checker.test'
)