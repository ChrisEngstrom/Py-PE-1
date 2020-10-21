#!/usr/bin/env python3

sumOfMultiples = 0

for i in range(3, 1000):
    if (i % 3 == 0 or
        i % 5 == 0):
        sumOfMultiples += i

print(sumOfMultiples)
