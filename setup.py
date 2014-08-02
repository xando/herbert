# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='herbert',
    author='Sebastian Pawluś',
    author_email='sebastian.pawlus@gmail.com',
    version="0.2",
    packages=['herbert'],
    description='An implmentation of herbert language',
    install_requires=["rply"],
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
