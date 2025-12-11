# coding: utf-8

"""
Wallee AG Python SDK

This library allows to interact with the Wallee AG payment service.

Copyright owner: Wallee AG
Website: https://en.wallee.com
Developer email: ecosystem-team@wallee.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "wallee"
VERSION = "6.3.0"
PYTHON_REQUIRES = ">=3.9"
REQUIRES = [
    "pydantic >= 2.10.4",
    "PyJWT >= 2.10.1",
    "python-dateutil >= 2.9.0.post0",
    "typing-extensions >= 4.12.2",
    "urllib3 >= 2.3, < 3",
    "cryptography >= 2.0"
]

EXTRAS_REQUIRE = {
    "dev": [
        "flake8 >= 7.1.1",
        "mypy >= 1.14.1",
        "pytest >= 3.9",
        "tox >= 4.23.2",
        "types-python-dateutil >= 2.9.0.20241206"
    ]
}

setup(
    name=NAME,
    version=VERSION,
    description="Wallee Group AG API",
    author="wallee",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Wallee Group AG API"],
    install_requires=REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    The Wallee Group AG API allows to create integrations, retrieve data and automate workflows.
    """,  # noqa: E501
    package_data={"wallee": ["py.typed"]},
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale"
    ]
)