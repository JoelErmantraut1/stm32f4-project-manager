#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: Joel Ermantraut
Last modified: 24/01/2020
Python version: 3.9.1

This script adds libraries to "Libraries" file,
which is included in Makefile to compile code
for STM32F4 boards.

If it receives:

    - Only a word, searches for it in standard libraries.
    - A file path, includes it.
    - A folder path, includes all .h and .c files in it.
"""

import glob
import os.path
import sys

HOME = os.path.expanduser('~')
LIBRARIES_FILE = "Location"
LIB_FILE_PATH = "Libraries"

def check_if_exists(string, file):
    """
    Checks if lib was already added.
    """
    for line in file.readlines():
        if string in line:
            return True

    return False

def add_lib_to_file(lib):
    """
    Add the given libraries to the Makefile libraries file.
    """
    string = "SRCS += {}\n".format(lib)
    with open(LIB_FILE_PATH, 'r+') as file:
        if not check_if_exists(lib, file):
            file.write(string)
            print("Library successfully added.")
        else:
            print("Library already in file.")

def list_libraries(path):
    """
    Returns all libraries in the folder.
    """
    return glob.glob(path + "/*.c")

def detect_type(lib):
    """
    Detects if it a standard lib, a path to a lib
    or a path to a folder.
    """
    if len(lib.split("/")) == 1:
        # Is a standard library
        with open(LIBRARIES_FILE, 'r') as file:
            LIBRARIES_PATH = file.read()

        LIBRARIES_PATH = "{}{}/{}".format(
                HOME,
                LIBRARIES_PATH.split('}')[-1][:-1],
                "Libraries/STM32F4xx_StdPeriph_Driver/src"
        )
        # The variable is set for Makefile
        # So we must get the important part

        for file in list_libraries(LIBRARIES_PATH):
            if lib in file:
                add_lib_to_file(os.path.basename(file))
                break

    elif len(lib.split("/")[-1].split(".")) > 1:
        # Is a file
        add_lib_to_file(lib)
    else:
        # Is a folder
        files = glob.glob(lib + "/*.c")
        files.extend(glob.glob(lib + "/*.h"))
        for file in files:
            add_lib_to_file(file)

def search_in_libs(lib_names):
    """
    Search for a file with the given name.
    It is very flexible, if it receives the
    complete filename, will find it. But if
    it receives only a part (what will be more
    usual), it will find it too.
    """

    for lib in lib_names:
        detect_type(lib)

def main():
    args = sys.argv[1:]

    search_in_libs(args)

if __name__ == "__main__":
    main()
