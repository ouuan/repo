#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-multidict-git']

def pre_build():
  pypi_pre_build(
    depends = ['python-multidict'],
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
  # moving to [community]
  # update_aur_repo()

if __name__ == '__main__':
  single_main()
