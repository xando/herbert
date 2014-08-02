# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='herbert',
    author='Sebastian Pawluś',
    author_email='sebastian.pawlus@gmail.com',
    version="0.1",
    packages=['herbert'],
    description='A implmentation of herbert language',
    entry_points={
        'console_scripts': [
            'herbert=herbert.main:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    zip_safe=False
)
