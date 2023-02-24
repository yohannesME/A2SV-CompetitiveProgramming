class MinStack(object):


    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        
        #handling the minstack
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)


    def pop(self):
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
                

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()