#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: Exercise 7 Question 1

import re
import sys

if sys.platform == "win32":
    filepath = r"C:\Windows\System32\drivers\etc\services"
elif sys.platform == "linux":
    filepath = r"/etc/services"

all_ports = set(range(1, 201))
used_ports = set()

with open(filepath, mode="rt") as df_open:
    for line in df_open:
        if line.startswith("#") or line == "": continue

        match = re.search(r"(\d+)/(tcp|udp)", line)

        if match:
            port = int(match.group(1))
            if port > 200: break
            used_ports.add(port)

unused_ports = (all_ports - used_ports)

print(unused_ports)