#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_provides(['libkate.so', 'liboggkate.so'])

def post_build():
    aur_post_build()
