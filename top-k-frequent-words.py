class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #Create a counter that keep count of all the elements but negative
        wordReverseCounter = defaultdict(int)

        for word in words:
            wordReverseCounter[word] -= 1
        
        # Add all the word and their negative count to the heap
        heap = []
        for word, reverseCount in wordReverseCounter.items():
            heap.append((reverseCount, word))
        
        heapify(heap)

        # hop the value and return the answer 
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
            
        return ans