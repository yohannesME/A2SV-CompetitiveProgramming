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
    n, maxDiff = get_ints()
    players = get_list()

    
    shuffleCount = 0
    
    def mergesort(left, right):
        nonlocal maxDiff
        
        if left + 1 == right:
            #two element are left
            if abs(players[left] - players[right]) > maxDiff:
                if players[left] > players[right]:
                    return [left+1]
                else:
                    return [right + 1]
            else:
                return [left+1, right+1]
                
        mid = (left + right)//2
        leftSide = mergesort(left, mid)
        rightSide = mergesort(mid + 1, right)
        
        #get the weakest winner from each side and see if the one from each side can beat them
        potentialWinner = []
        leftWeakWinner = players[min(leftSide, key=lambda index: players[index-1])-1]
        for rightWinner in rightSide:
            if abs(players[rightWinner-1] - leftWeakWinner) > maxDiff:
                if players[rightWinner-1] > leftWeakWinner:
                    potentialWinner.append(rightWinner)
            else:
                potentialWinner.append(rightWinner)
        
            
        rightWeakWinner = players[min(rightSide, key=lambda index: players[index-1])-1]
        for leftWinner in leftSide:
            if abs(players[leftWinner-1] - rightWeakWinner) > maxDiff:
                if players[leftWinner-1] > rightWeakWinner:
                    potentialWinner.append(leftWinner)
            else:
                potentialWinner.append(leftWinner)
        
        return potentialWinner
        
            
    
    return mergesort(0, len(players)-1)

if __name__ == "__main__":
    print(*sorted(solve()))