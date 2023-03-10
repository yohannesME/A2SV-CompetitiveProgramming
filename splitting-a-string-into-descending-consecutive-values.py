class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(index, currentValue=[]):
            if index >= len(s):
                return len(currentValue) >= 2
            


            for i in range(index, len(s)):
                value = int(s[index:i+1])

                if not currentValue or value + 1 == currentValue[-1]:
                    currentValue.append(value)
                
                    if backtrack(i+1, currentValue):
                        return True
                    currentValue.pop()
        return backtrack(0)