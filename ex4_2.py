#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: Exercise 4 question 2

for line in open(r'C:\labs\messier.txt', encoding='latin_1'):
    if not line: break
    if line.startswith("M"):
        # Slice each field
        mes_num = line[:6].rstrip()
        com_name = line[6:40].rstrip()
        if not com_name: com_name = "no name"
        obj_type = line[40:64].rstrip()
        const = line[64:].rstrip()
        print(f"|{mes_num}|{com_name}|{obj_type}|{const}|")