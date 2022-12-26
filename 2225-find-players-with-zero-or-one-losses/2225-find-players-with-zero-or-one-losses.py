class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #the answer and fullmatch array of all the winners and loosers
        answer = []
        fullmatch = []
        
        
        #zip all the wins and looses together
        for match in zip(*matches):
            fullmatch.append(list(match))
        
        #first create a set of winners diffence the losers
        answer.append(set(fullmatch[0]))
        
        answer[0] = answer[0].difference(set(fullmatch[1]))
        answer[0] = list(answer[0])
        
        #dictionary to keep count of all the loosers repetition
        loosercount = Counter(fullmatch[1])
        
        #add the  number if its count is one
        answer.append([])
        
        for num, count in loosercount.items():
            if count == 1:
                answer[1].append(num)
        
        #sort the answer
        answer[0].sort()
        answer[1].sort()
        
        return answer