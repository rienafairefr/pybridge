# coding: utf-8
"""
pybridge setup.py
"""

import os

from setuptools import setup

NAME = "pybridge"
VERSION = os.environ.get('TRAVIS_TAG', os.environ.get('TAG_NAME', 'dev'))

REQUIRES = ["sqlalchemy"]

setup(
    name=NAME,
    version=VERSION,
    long_description="""This is pybridge, SQLAlchemy and API to use the Fintech Bridge API https://bridgeapi.io/

""",
    long_description_content_type='text/markdown',
    author='rienafairefr',
    author_email="rienafairefr@gmail.com",
    url="https://www.github.com/rienafairefr/pybridge/",
    keywords=["bridge API"],
    install_requires=REQUIRES,
)
