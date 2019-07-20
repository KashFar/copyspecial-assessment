#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Kash Farhadi"


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    """returns a list of the absolute paths of the special files in the given directory"""
    output = [filename for filename in os.listdir(dir) if re.search(
        '__(.[A-Za-z]*)__', filename)]
    return output

def copy_to(paths, dir):
    """ Given a list of paths, copies those files into the given directory"""
    pass


def zip_to(paths, zippath):
    """ Given a list of paths, zip those files up into the given zipfile"""
    pass


def main():
    """ Copies, compresses, or prints special files"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('from_dir', help="source dir for copy")
    args = parser.parse_args()

    special_paths=get_special_paths(args.from_dir)

    if not args.todir and not args.tozip:
        for filename in special_paths:
            print(filename)

    


if __name__ == "__main__":
    main()
