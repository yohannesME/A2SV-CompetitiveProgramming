#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    size = len(a)
    swap = 0
    for i in range(size):
        for j in range(0,size-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap += 1
    print('Array is sorted in',swap, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
