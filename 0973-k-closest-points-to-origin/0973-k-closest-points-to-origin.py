class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #calculated distance
        distance = []
        
        #answer to hold the least distance
        answer = []
        
        #calculate the distance and store in a 2d array of the x,y and the distance to origin
        for point in points:
            dist = abs(point[0]**2 + point[1]**2)
            distance.append([dist, point])
        
        #create a min heap to store the distances and take the first k closest points
        heapq.heapify(distance)
        for _ in range(k):
            answer.append(heapq.heappop(distance)[1])

        return answer
        
        