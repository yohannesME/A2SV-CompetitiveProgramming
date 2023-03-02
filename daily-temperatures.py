class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        answer = [0]*N

        stack = []
        i = 0

        while i < N:
            if len(stack) == 0:
                stack.append([i, temperatures[i]])
                i += 1
            elif stack[-1][1] >= temperatures[i]:
                stack.append([i, temperatures[i]])
                i += 1
            else:
                index = stack.pop()[0]
                answer[index] = i-index
                
        return answer