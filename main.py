"""
This file is for our new theme: a program that separates files by type (docs, pdf, jpg, etc.).
Create by: Miqayel Postoyan
Date: 30 April
"""
import os
import shutil


def main():
    """
    Function: main
    Brief: Entry point
    """
    noqcel = ["main.py", "vnev"]
    cwd = os.getcwd()
    for i in os.listdir(cwd):
        if i in noqcel[0] and i in noqcel[1]:
            if i.split(".")[-1] not in os.listdir(cwd):
                os.mkdir(i.split(".")[-1])
            if i.split(".")[-1] in os.listdir(cwd):
                shutil.move(i, cwd + "/" + i.split(".")[-1])


if __name__ == "__main__":
    main()
