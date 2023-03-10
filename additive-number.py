class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backtrack(index, currentSumList=[]):

            if index >= len(num):
                return len(currentSumList) >= 3 and currentSumList[-1] == currentSumList[-2]+currentSumList[-3]

            for i in range(index, len(num)):
                newValue = num[index:i+1]
                if  len(newValue) > 1 and newValue[0] == '0':
                    continue

                value = int(newValue)
                if len(currentSumList) < 2 or value == currentSumList[-2]+currentSumList[-1]:
                    currentSumList.append(value)
                    if backtrack(i+1, currentSumList):
                        return True
                    currentSumList.pop()

        return backtrack(0)