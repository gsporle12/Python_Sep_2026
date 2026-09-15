#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: This script will generate 6 random lottery numbers
import random

lotto = [] # Create an empty list

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number generated: ", num)

print("Lottery numbers =", lotto)