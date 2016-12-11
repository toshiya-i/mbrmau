# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="mbrmau",
    version="0.1.0",
    entry_points={
        "console_scripts": ['mbrmau = mbrmau:main']
    },
    description="mbrmau - make a base of request mail for account unlock.",
    license="MIT",
    author="toshiya-i",
    packages=find_packages(exclude=['tests*']),
    install_requires=["Jinja2", "python-dateutil"],
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ]
)
