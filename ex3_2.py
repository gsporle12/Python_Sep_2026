#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: Write a Python program to display a range of numbers by steps of -2.
import sys

var = input("Please enter an integer: ")

if not var.isdecimal():
    # Validate the input
    print("Please enter a valid positive integer")
    sys.exit()

var = int(var) # Convert the input to an integer.

for number in range(var, -1, -2):
    print(number)