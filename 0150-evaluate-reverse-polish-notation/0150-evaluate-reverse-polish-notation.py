class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t.lstrip('-+').isdigit():
                print(int(t))
                stack[:0] = [int(t)]
            else:
                temp = eval(str(stack[1])+t+str(stack[0])+".0")
                del stack[0]
                del stack[0]
                stack[:0] = [int(temp)]
        return stack[0]
        