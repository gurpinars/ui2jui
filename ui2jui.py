#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Small tool to convert qt designer ui files to .jui format which is required
for qt to use with java language.
"""

import argparse
import os


def convert(ui_file):
    fname = "%s.jui" % os.curdir.join(ui_file.split('.')[:-1])

    with open(ui_file, "r") as f:
        lines = f.readlines()
        del(lines[0:1])
        lines[0] = '<ui version="4.0" language="jambi">\n'

    with open(fname,'w') as fout:
        for line in lines:
            fout.write(line)


def main():
    parser = argparse.ArgumentParser(description="converter from .ui files to .jui")
    parser.add_argument('-f', '--file', help='ui file to be converted')
    parser.add_argument('-d', '--directory', help='convert all files of curdir', action="store_true")
    parser.add_argument('-r', '--recursive', help='convert all .ui files of curdir', action="store_true")
    parser.add_argument('-rm', '--remove', help='remove file after converted', action='store_true')
    args = parser.parse_args()
    if args.recursive:
        for file in get_ui_files_from_dir_recursively():
            convert(file)
        if args.remove:
            for file in get_ui_files_from_dir_recursively():
                del_file(file)
        print "converted"

    elif args.directory:
        for file in get_ui_files_from_dir():
            convert(file)
        if args.remove:
            for file in get_ui_files_from_dir():
                del_file(file)
        print "converted"

    elif not (args.file == None):
        convert(args.file)
        if args.remove:
            del_file(args.file)
        print "converted"

def is_file_ends_with_ui(filename):
    return filename.split('.')[-1] == "ui"

def get_ui_files_from_dir():
    return [file for file in os.listdir('.') if is_file_ends_with_ui(file)]

def del_file(file):
    os.remove(file)


def get_ui_files_from_dir_recursively():
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk('.') for f in filenames if is_file_ends_with_ui(f)]

if __name__ == '__main__':
    main()
