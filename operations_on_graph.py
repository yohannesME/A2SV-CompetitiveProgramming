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
    k = get_int()
    graph = defaultdict(list)
    
    def vertex(v):
        print(*graph[v])

    def addEdge(u,v):
        graph[u].append(v)
        graph[v].append(u)
    
    for _ in range(k):
        operation = get_list()
        if operation[0] == 1:
            addEdge(operation[1], operation[2])
        else:
            vertex(operation[1])

        
        
if __name__ == "__main__":
    solve()