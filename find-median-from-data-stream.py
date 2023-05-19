class MedianFinder:

    def __init__(self):
        self.minHeap = [float('inf')]
        self.maxHeap = [float('inf')]
        

    def addNum(self, num: int) -> None:
        if num <= -self.minHeap[0]:
            heappush(self.minHeap, -num)
            if len(self.minHeap) > len(self.maxHeap)+1:
                heappush(self.maxHeap, -heappop(self.minHeap))
            return
        
        if num >= self.maxHeap[0]:
            heappush(self.maxHeap, num)
            if len(self.maxHeap) > len(self.minHeap)+1:
                heappush(self.minHeap, -heappop(self.maxHeap))
            return
        

        if len(self.minHeap) <= len(self.maxHeap):
            heappush(self.minHeap, -num)
        else:
            heappush(self.maxHeap, num)
        

    def findMedian(self) -> float:
        minlen = len(self.minHeap)
        maxlen = len(self.maxHeap)

        if minlen > maxlen:
            return -self.minHeap[0]
        elif minlen < maxlen:
            return self.maxHeap[0]
        else:
            return (self.maxHeap[0] - self.minHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()