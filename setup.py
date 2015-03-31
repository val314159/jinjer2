#!/usr/bin/env python
import os,sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#if sys.version_info < (2,5):
#    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use jinjer2.")

import jinjer2

setup(
    name = "Jinjer2",
    version = jinjer2.__version__,
    py_modules=['jinjer2'],
    entry_points = dict(
        console_scripts=['jinjer2=jinjer2:main'],
    ),
    #scripts=['jinjer2'],
    #scripts=['xxx'],
    install_requires = ['Jinja2==2.7.3',
                        'pyaml==15.3.1',
                    ],
    description = "Static Macro File Generator (cmd line generator using jinja2)",
    long_description = jinjer2.__doc__,
    author = jinjer2.__author__,
    author_email = "jmward@gmail.com",
    platforms='any',
    license = "Apache",
    keywords = "jinja2 static file generator macro",
    url = "https://github.com/val314159/jinjer2",
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
    ]
)
