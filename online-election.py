class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.answers = []
        count = defaultdict(int)
        answer = [0,0]
        for i in range(len(persons)):
            count[self.persons[i]] += 1

            if count[self.persons[i]] >= answer[1]:
                answer = [self.persons[i], count[self.persons[i]]]
            self.answers.append(answer[0])

    def getHighest(self, index):
        return self.answers[index]


    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1

        while left < right:
            mid = (left + right)//2

            if self.times[mid] < t:
                left = mid + 1
            else:
                right = mid 
        index = left if self.times[left] <= t else left - 1

        return self.getHighest(index)
    

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)