#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arg=[]
    for i in arr:
        a=arr[1]+arr[2]+arr[3]+arr[4]
        b=arr[0]+arr[2]+arr[3]+arr[4]
        c=arr[0]+arr[1]+arr[3]+arr[4]
        d=arr[0]+arr[1]+arr[2]+arr[4]
        e=arr[0]+arr[1]+arr[2]+arr[3]
    arg.append(a)
    arg.append(b)
    arg.append(c)
    arg.append(d)
    arg.append(e)
    print(min(arg), max(arg))
    

    




if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
