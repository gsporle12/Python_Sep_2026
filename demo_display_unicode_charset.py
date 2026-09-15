#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: Demonstrates HOWTO display the entire unicode charset in a terminal window.

#Iterate through all the unicode char positions.
for pos in range(0,65536):
    try:
        print(pos, chr(pos), end=" ")
    except UnicodeEncodeError:
        print(" ")