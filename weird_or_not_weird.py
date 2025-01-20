#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 6:
        print('Not Weird') 
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird') 
    elif n % 2 == 0 and n >= 20:
        print('Not Weird')

# Notes on Range Checks:
# 1. To check if a number falls within an inclusive range, use the syntax:
#    X <= value <= Y
#    Example: if 2 <= n <= 6:
#             print("In range 2 to 6")
# 2. To check an exclusive range, use:
#    X < value < Y
#    Example: if 2 < n < 6:
#             print("In exclusive range 2 to 6")
