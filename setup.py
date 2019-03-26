#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='my-pmi-custom-models',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pmlib@https://pmi-dev-cluster.us-south.containers.appdomain.cloud/ibm/pmi/service/rest/ds/08e5ad71/d0vsppa2/lib/download?filename=pmlib-1.2.0-master.tar.gz'
    ]
)
