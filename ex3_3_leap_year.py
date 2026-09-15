#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: Returns if the entered year is a leap year.
import sys

year = input("Please enter a year: ")

if not year.isdecimal():
    # Validate the input
    print("Please enter a valid year")
    sys.exit()

year = int(year)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Year {year} is a leap year!")
else:
    print(f"Year {year} is not a leap year.")
