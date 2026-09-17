#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: Exercise 8

def my_func(value, alist=None):
    """
    Appends value to the list of alist and then prints the list
    :param value: any value
    :param alist: empty list
    :return:
    """
    alist=[]
    alist.append(value)
    print(alist)
    return

my_func("hello")
my_func("my")
my_func("name")
my_func("is")
my_func("george")
my_func(3.14)

