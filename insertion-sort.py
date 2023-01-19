#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):

    key = arr[n-1]
    for i in range(n-2, -1,-1):
        j = i 
 
        if ( arr[j] > key):
            arr[j + 1] = arr[j]
            j = j - 1
            for k in range(n):
                print(arr[k], end=' ')
                
            print()           
        else:
            arr[j + 1] = key;
            for k in range(n):
                print(arr[k], end=' ')
                
            print()  
            
            break;
        
        if(i==0):
            arr[0] = key
            
            for k in range(n):
                print(arr[k], end=' ')
                
            print()  
            
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
