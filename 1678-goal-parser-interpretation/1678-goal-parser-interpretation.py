class Solution:
    def interpret(self, command: str) -> str:
        #stack to keep track of the elements in the bracket
        stack = []
        
        #iterate through the command letter and parse () and (al)
        for c in command:
            if c == ')':
                if stack[-1] == '(':
                    stack[-1] = 'o'
                else:
                    del stack[-3:]
                    stack.append('al')
            else:
                stack.append(c)
        return ''.join(stack)