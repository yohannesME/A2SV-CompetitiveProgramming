class Solution:
    def findFrequency(self, word):
        freq = 1
        smallest = word[0]
        for i in range(1, len(word)):
            if smallest > word[i]:
                smallest = word[i]
                freq = 1
            elif smallest == word[i]:
                freq += 1
        
        return freq

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        #find the frequency of the lexically small element of the words and also the queries
        wordFreq = []
        for word in words:
            wordFreq.append(self.findFrequency(word))
        wordFreq.sort(reverse=True)
        queryFreq = []
        for query in queries:
            queryFreq.append(self.findFrequency(query))
        
        answer = []
        N = len(wordFreq)

        for query in queryFreq:
            left = 0
            right = N-1

            while left < right:
                mid = (left+right)//2
                if wordFreq[mid] > query:
                    left = mid + 1
                else:
                    right = mid 
            #handle the edge case that is one element is present
            answer.append(left+1 if wordFreq[left] > query else left)

        return answer