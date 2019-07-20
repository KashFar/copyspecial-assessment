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
import sys
import commands



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
    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(os.path.abspath(dir))
    for path in paths:
        shutil.copy(path, os.path.abspath(dir))
            

def zip_to(zippath):
    command = 'zip -j {} '.format(zippath)
    print 'Command being run:', command
    (status, output) = commands.getstatusoutput(command)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print output   


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
    elif args.todir:
        copy_to(special_paths, args.todir)
    elif args.tozip:
        copy_to(special_paths, 'temp')
        zip_to(args.tozip)
           

if __name__ == "__main__":
    main()
