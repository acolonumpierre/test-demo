#!/usr/bin/env python

import sys

print sys.argv


def sum_digits(n):

    sum = 0

    while n > 0:
        digit = n%10
        sum += digit
        n /= 10
    return sum

if len(sys.argv) >= 3:
    j = sys.argv[2]
else:
    j = sys.argv[1]

print j
    
for i in range(1, j):
    num = i*n
    total = sum_digits(num)
    print total
