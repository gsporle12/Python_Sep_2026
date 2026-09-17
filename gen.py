#! /usr/bin/env python3
# Author: GSporle
# Version: 1.0
# Description: For exercise 9 question 1

def frange(start, stop, step=0.25):

    if step == 0:
        return

    start = float(start)
    stop = float(stop)
    step = float(step)

    current = 0

    while True:
        value = start + current * step

        if step > 0 and value >= stop:
            break
        if step < 0 and value <= stop:
            break

        yield value
        current += 1


print(list(frange(1.1, 3)))
print("-" * 50)
print(list(frange(1, 3, 0.33)))
print("-" * 50)
print(list(frange(1, 3, 1)))
print("-" * 50)
print(list(frange(3,1)))
print("-" * 50)
print(list(frange(1, 3, 0)))
print("-" * 50)
print(list(frange(-1, -0.5, 0.1)))
print("-" * 50)

for num in frange(3.142, 12):
    print(f"{num:05.2f}")
print("-" * 50)
print(frange(1,2))