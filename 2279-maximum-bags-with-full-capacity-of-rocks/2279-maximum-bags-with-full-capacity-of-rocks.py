class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # the number of rocks needed to fill a container
        availableCapacity = []
        N = len(capacity)

        #create array of rocks needed to fill a specific bag
        for i in range(N):
            availableCapacity.append(capacity[i]-rocks[i])
        
        #sort that we first handle smallest needs
        availableCapacity.sort()
        
        #when the bag is full takes the additional rocks and 
        #use them to fill the available slots
        for index,available in enumerate(availableCapacity):
            additionalRocks -= available
            if additionalRocks == 0:
                return index+1
            elif additionalRocks < 0:
                return index
            
        return N
        