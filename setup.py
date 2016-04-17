#!/usr/bin/env python

from setuptools import setup


setup(
    name="hne",
    version="1.0",
    py_modules=["hne"],
    entry_points={
        "console_scripts": ["hne = hne:main"],
    },
)
