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

def possibleBipartition( n, edges):
    #create a adjacecy list for a dfs
    adjList = {}
    for i in range(n):
        adjList[i] = []
    #one for the offset initialize our colors
    colors = [-1]*(n)


    for v1, v2 in edges:
        adjList[v1-1].append(v2-1)
        adjList[v2-1].append(v1-1)

    def bfs_bicolor(graph):
        colors = {}
        queue = []
        for node in graph:
            if node not in colors:
                colors[node] = 1
                queue.append(node)
                while queue:
                    curr = queue.pop(0)
                    for neighbor in graph[curr]:
                        if neighbor not in colors:
                            colors[neighbor] = 3 - colors[curr]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[curr]:
                            return False
        return True
    return bfs_bicolor(adjList)
    


def solve():
    while True:   
        n= get_int()
        if n == 0:
            break
        
        edgeCount = get_int()
        edges = []
        for _ in range(edgeCount):
            edges.append(get_list())
        if possibleBipartition(n, edges):
            print('BICOLOURABLE.')
        else:
            print('NOT BICOLOURABLE.')
        
if __name__ == "__main__":
    solve()