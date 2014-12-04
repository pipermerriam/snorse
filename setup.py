#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='snorse',
    version='1.0.0',
    description='Unicode Snowman Morse Code',
    long_description=readme + '\n\n' + history,
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/pipermerriam/snorse',
    py_modules=[
        'snorse',
    ],
    entry_points={
        'console_scripts': [
            "snorse=snorse:snorse_cli",
            "desnorse=snorse:desnorse_cli",
        ],
    },
    install_requires=['click==3.3'],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='snorse',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
