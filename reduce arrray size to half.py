class Solution(object):
    def minSetSize(self, arr):
        count = collections.Counter(arr)

        result = 0
        answerCount = 0

        values = list(count.values())
        values.sort(reverse=True)

        for i in range(len(values)):
            answerCount += 1
            result+=values[i]
            if(result >= (len(arr)/2)):
                break

                    
        return answerCount
        
