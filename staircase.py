#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    a="#"
    width=n
    print(a.rjust(width))
    if n in range(0,101):
        for i in range(0,n-1):
            
            a="#"+a
            
            print(a.rjust(width))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
