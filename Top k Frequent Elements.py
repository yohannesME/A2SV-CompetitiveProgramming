class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)

        values = list(count.values())
        values.sort()

        answer = []

        for i in range(1, k+1):
            reptition = values[len(values)-i]

            for key in count.keys():
                if(count[key] == reptition):
                    answer.append(key)
                    count[key] = 0
                    break

        return answer
