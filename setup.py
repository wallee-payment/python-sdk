# coding: utf-8

import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

NAME = "wallee"
VERSION = "5.1.0"

REQUIRES = [
    "certifi >= 14.05.14",
    "six >= 1.10",
    "python_dateutil >= 2.8.2",
    "setuptools >= 68.0.0",
    "urllib3 >= 2.0.7",
    "cryptography >= 2.0"
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Wallee AG",
    description="SDK that allows you to access wallee",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["wallee", "Payment", "Payment Integration"],
    install_requires=REQUIRES,
    include_package_data=True,
    license='Apache-2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial :: Point-Of-Sale',
    ],
    python_requires='>=3.7',
)
