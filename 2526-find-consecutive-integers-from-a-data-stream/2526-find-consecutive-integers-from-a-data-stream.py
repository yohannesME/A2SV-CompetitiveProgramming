class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.different = -1
        self.data = deque()

    def consec(self, num: int) -> bool:
        self.data.appendleft(num)
        # we have a difference variable to hold the last straying variable and calculate from that point if have enough lenght which is k to return true
        if num != self.value:
            self.different = len(self.data)
            return False
        else:
            if self.different == -1:
                return len(self.data) >= self.k
            return len(self.data)-self.different >= self.k
            
        # if len(self.data)+1 < self.k:
        #     self.data.appendleft(num)
        #     return False
        # else:
        #     self.data.appendleft(num)
        #     for i in range(self.k):
        #         if self.data[i] != self.value:
        #             return False
        #     return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)