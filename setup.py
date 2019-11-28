"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='push_app_version',
    version='0.0.1',  # Required
    description='Push version in GCS bucket for triggered deployments',
    long_description='Trigger deploys from Concourse CI',
    url='https://github.com/mrpink/push-app-version',
    author='Will Pink',
    keywords='google gcs version',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=[
        'google-cloud-storage'
    ],
    entry_points={  # Optional
        'console_scripts': ['push-app-version=push_version.push:main'],
    },
)
