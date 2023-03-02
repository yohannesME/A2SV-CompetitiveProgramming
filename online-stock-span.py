class StockSpanner:

    def __init__(self):
        self.stack = []
        self.data = []
        

    def next(self, price: int) -> int:
        #pop the element from the stack that is less and check the index different 
        self.data.append(price)
        while self.stack and self.data[self.stack[-1]] <= price:
            self.stack.pop()

        self.stack.append(len(self.data)-1)


        if len(self.stack) > 1:
            return self.stack[-1] - self.stack[-2]
        else:
            return len(self.data)
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)