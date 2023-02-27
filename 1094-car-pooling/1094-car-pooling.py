class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #1000 is the maximum distance traveled 0 indexed so 1 for offset
        ongoingTrip = [0]*1000
        
        #check if the first trip is greater than capacity as we skip that
        if trips[0][0] > capacity:
            return False
        
        #just ready the prefix sum by placing the start and end of the trip
        for trip in trips:
            ongoingTrip[trip[1]-1] += trip[0]
            ongoingTrip[trip[2]-1] -= trip[0]
        
        
        
        #update the trip for all the value if capacity passed check
        for i in range(1, 1000):
            ongoingTrip[i] += ongoingTrip[i-1]
            if ongoingTrip[i] > capacity:
                return False
        
        return True
            