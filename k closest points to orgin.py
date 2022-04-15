import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point=[]
        distance = {}
        i = 0
        for cord in points:
            distance[i] = math.sqrt(cord[0]*cord[0]+cord[1]*cord[1])
            i = i + 1

        distance = sorted(distance.items(), key =lambda d:d[1])

        for(key, value) in distance[:k]:
            point.append(points[key]);

        return point
