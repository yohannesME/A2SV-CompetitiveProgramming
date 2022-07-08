class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in range(len(pushed)):
            if pushed[i] == popped[0]:
                popped.pop(0)
                for j in range(len(stack)):
                    if stack[len(stack)-1] == popped[0]:
                        popped.pop(0)
                        stack.pop(-1)
                        
                    else:
                        break
            else:
                stack.append(pushed[i])    
        stack.reverse()
        print(stack, popped)
        for i in range(len(stack)):
            if stack[i] != popped[i]:
                return False
        return True
