#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@polyaxon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import find_packages, setup  # noqa: H301

NAME = "polyaxon-sdk"
VERSION = "1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["certifi>=2017.4.17", "python-dateutil>=2.1", "six>=1.10", "urllib3>=1.23"]


setup(
    name=NAME,
    version=VERSION,
    description="Polyaxon SDKs and REST API specification.",
    author_email="contact@polyaxon.com",
    url="",
    keywords=["Swagger", "Polyaxon SDKs and REST API specification."],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Polyaxon SDKs and REST API specification.  # noqa: E501
    """,
)
