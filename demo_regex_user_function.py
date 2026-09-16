#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: This script will demo HOWTO define a REUSABLE function for
# searching for Regex Patterns in one or more files.

import re

# Example of a user function with optional parameter passing
# and default values, and optional return value (lines matched)
def search_pattern(pattern=r"^.{19}$", file=r"C:\labs\words"):
    fh_in = open(file, mode="rt")
    lines = 0
    reobj = re.compile(pattern) # Compiles pattern ONLY ONCE

    for line in fh_in:
        m = reobj.search(line) # Match using PRECOMPILED Pattern
        if m:
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
            lines += 1

    fh_in.close()
    return lines

search_pattern()
num_lines = search_pattern(r"^([A-Z]).*\1$", r"C:\labs\words")
print(f"Matched {num_lines} lines")