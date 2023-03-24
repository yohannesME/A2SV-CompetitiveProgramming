import sys
import math
import bisect
import heapq
import itertools
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right

mod=1000000007

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))

def solve():
    n = get_int()
    tree = get_list()
    
    if n == 1:
        return 0
    
    shuffleCount = 0
    
    def mergesort(left, right):
        nonlocal shuffleCount
        
        if left + 1 == right:
            #two element are left
            if tree[left] > tree[right]:
                tree[left], tree[right] = tree[right], tree[left]
                shuffleCount += 1
            return
                
        mid = (left + right)//2
        mergesort(left, mid)
        mergesort(mid + 1, right)

        if tree[left] > tree[right]:
            firststart = left
            secondstart = mid + 1
            while firststart < mid + 1:
                tree[firststart], tree[secondstart] = tree[secondstart], tree[firststart]
                firststart += 1
                secondstart += 1
            shuffleCount += 1
    
        for i in range(left, right):
            if tree[i] > tree[i+1]:
                shuffleCount = -1
                break
    
    mergesort(0, n-1)
    return shuffleCount

if __name__ == "__main__":
    for _ in range(get_int()):
        print(solve())