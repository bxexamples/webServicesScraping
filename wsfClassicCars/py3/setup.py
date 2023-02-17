#!/usr/bin/env python

import setuptools
#import sys

def readme():
    with open('TITLE.txt') as f:
         return f.readline().rstrip('\n')

def longDescription():
    with open('README.rst') as f:
         return f.read()


#from setuphelpers import get_version, require_python
#from setuptools import setup


#__version__ = get_version('unisos/icm/__init__.py')
__version__ = '0.1'


requires = [
    "unisos.wsf"
]


#print('Setting up under python version %s' % sys.version)
#print('Requirements: %s' % ','.join(requires))

scripts = [
    "./bin/scraperClassicCars.py",
    "./bin/classicCarsScraperParams.py",
    "./bin/scrapeExample.py",
    "./bin/icmClassicCarsWebScraper.py",
]


setuptools.setup(
    name='unisos.wsfClassicCars',
    version=__version__,
    namespace_packages=['unisos'],
    packages=setuptools.find_packages(),
    scripts=scripts,
    include_package_data=True,
    zip_safe=False,
    author='Mohsen Banan',
    author_email='libre@mohsen.1.banan.byname.net',
    maintainer='Mohsen Banan',
    maintainer_email='libre@mohsen.1.banan.byname.net',
    url='http://www.by-star.net/PLPC/180047',
    license='AGPL',
    description=readme(),
    long_description=longDescription(),
    download_url='http://www.by-star.net/PLPC/180047',
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )

