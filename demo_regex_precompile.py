#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: This script will demo HOWTO match text using str testing and
# pattern matching using Regex and re.py module.

import re
fh_in = open(r"C:\labs\words", mode="rt")

reobj = re.compile(r"^.{19}$") # Compiles pattern ONLY ONCE

for line in fh_in:
    # m = re.search(r"^.{19}$", line)  # Match lines with exactly 19 chars
    m = reobj.search(line)  # Match using PRECOMPILED Pattern
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")

fh_in.close() # Close file handle.
