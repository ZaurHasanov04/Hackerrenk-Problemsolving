#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ar=[]
    reqema=0
    reqemb=0
    
    c=a[0]-b[0]
    d=a[1]-b[1]
    e=a[2]-b[2]
    
    
    
    if c>0 :
        reqema=0+1
   
    if c<0:
        reqemb=0+1
    
        
    
    if d>0 :
        reqema=reqema+1 
   
    if d<0:
        reqemb=reqemb+1
    
        

    if e>0 :
        reqema=reqema+1 
   
    if e<0:
        reqemb=reqemb+1

    ar.insert(0, reqema)
    ar.insert(1, reqemb)
    
    
     
    return ar

    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
