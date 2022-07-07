class Solution(object):
    def isValid(self, s):
        stack = []
        for par in s:
            if par == '(':
                stack.append('(')
            elif par == ')':
                if len(stack) > 0:
                    if(stack[-1] == '('):
                        del stack[-1]
                    else:
                        return False
                else:
                    return False
            if par == '{':
                stack.append('{')
            elif par == '}':
                if len(stack) > 0:
                    if(stack[-1] == '{'):
                        del stack[-1]
                    else:
                        return False
                else:
                    return False
            if par == '[':
                stack.append('[')
            elif par == ']':
                if len(stack) > 0:
                    if(stack[-1] == '['):
                        del stack[-1]
                    else:
                        return False
                else:
                    return False

        print(stack)
            
        return len(stack)==0
