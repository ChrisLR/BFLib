"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='BFLib',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='A library based on the Basic Fantasy Rpg',
    author='Chris LR',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(),
    # install_requires=[''],
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},
    #package_data={
    #    'sample': ['package_data.dat'],
    #},
    #entry_points={
    #   'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},
)