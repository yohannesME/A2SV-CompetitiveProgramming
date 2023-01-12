class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #populate the number in an array
        participant = [i+1 for i in range(n)]
        
        # remove while they are encoutered
        index = 0
        while len(participant) > 1:
            index =(index + k-1)%n
            del participant[index]
            n -= 1
            
        
        return participant[0]