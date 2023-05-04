class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-10000]

        for num in nums:
            if len(self.heap) < k:
                heappush(self.heap, num)
            else:
                heappushpop(self.heap, num)


    def add(self, val: int) -> int:
        heappushpop(self.heap, val)
        return self.heap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)