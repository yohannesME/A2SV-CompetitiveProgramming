import sys
import math
import bisect
import heapq
import itertools
from sys import stdin,stdout
from math import gcd,floor,sqrt,log, ceil
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right

mod=1000000007

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))

def solve():
    n= get_int()
    adjacentList = []
    for _ in range(n):
        adjacentList.append(get_list())
    #sink => row
    #source => column
    sink = []
    source = []
    
    for row in range(n):
        if sum(adjacentList[row]) == 0:
            sink.append(row+1)
            
    for column in range(n):
        colSum = 0
        for row in range(n):
            colSum += adjacentList[row][column]
        if colSum == 0:
            source.append(column + 1)
    
    print(len(source), *source)
    print(len(sink), *sink)
        
        
        
if __name__ == "__main__":
    solve()
