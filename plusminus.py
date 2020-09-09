#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arp=[]
    arm=[]
    arz=[]
    if n in range(0,101):
        for i in arr:
            if i in range(-100,101):
                if i>0:
                    arp.append(i)
                elif i<0:
                    arm.append(i)
                elif i==0:
                    arz.append(i)
            else:
                print("bele sey yoxdu")

    a=len(arp)/n
    b=len(arm)/n
    c=len(arz)/n

    print("{:f} ".format(a))
    print("{:f} ".format(b))
    print("{:f} ".format(c))

    

    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
