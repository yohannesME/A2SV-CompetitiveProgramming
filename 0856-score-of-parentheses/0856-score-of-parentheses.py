class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scoreStack = []
        output = 0

        for brace in s:
            if brace == '(':
                scoreStack.append('(')
            else:
                if scoreStack[-1] == '(':
                    scoreStack[-1] = 1
                else:
                    #if we find a parent paranthesis then add up the child and multiply them by 2
                    paranth = 0
                    while scoreStack[-1] != '(':
                        paranth += scoreStack.pop()
                    scoreStack.pop()
                    scoreStack.append(paranth*2)
            
        return sum(scoreStack)