#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: This script will demo HOWTO match text using str testing and
# pattern matching using Regex and re.py module.

import re

# Open file handle for READING in TEXT mode.
fh_in = open(r"c:\labs\words", mode="rt")

# Iterate through the file handle reading one line at a time
# using an ITERATOR for loop.
for line in fh_in:
    #Example of str testing
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    #Example of Regex testing
    # m = re.search(r"^the", line) # Match lines starting with "the"
    # m = re.search(r"ing$", line) # Match lines ENDING with "ing"
    # m = re.search(r"^.ing$", line) # Match lines with 4 chars ENDING with "ing"
    # m = re.search(r"^[adpr]ing$", line)  # Match lines with 4 chars starting with A,D,P,R ending in "ing"
    # m = re.search(r"^[^dz]ing$", line)  # Match lines with 4 chars not starting with D,Z ending in "ing"
    # m = re.search(r"^[A-Z]ing$", line)  # Match lines STARTING with a capital and ending in "ing"
    # m = re.search(r"^...................$", line)  # Match lines exactly 19 characters
    # m = re.search(r"^.{19}$", line)  # Match lines exactly 19 characters
    # m = re.search(r"^...................", line)  # Match lines at least 19 characters
    # m = re.search(r"\.", line) # Match lines with a DOT
    # m = re.search(r"[.]", line) # Match lines with a DOT
    # m = re.search(r"[aeiou][aeiou][aeiou]", line) # Match lines with 3 consecutive VOWELS
    # m = re.search(r"[aeiou]{4}", line) # Match lines with 4 consecutive VOWELS
    # m = re.search(r"^[A-Z].*[A-Z]$", line) # Match lines START/END with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line) # Match lines START/END with a CAPITAL with 4 chars in between
    m = re.search(r"^(.)(.).\2\1$", line) # Match lines 5 char palindromes
    # m = re.search(r"([A-Z]).*\1$", line) # Match lines START/END with the SAME CAPITAL

    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}, "
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")

fh_in.close() # Close file handle.
