class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.data = []

    def consec(self, num: int) -> bool:
        self.data.append(num)
        # we clear the array when we encounter different value then value, hence use the length to check
        if num != self.value:
            self.data = []
            return False
        else:
            return len(self.data) >= self.k
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)