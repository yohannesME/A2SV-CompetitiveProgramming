class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #lower case alphabet
        alphabet = list(list(string.ascii_lowercase))
        N = len(s)
        answer = []
        #the index of the alphabet for a o(1) access
        alphabetIndex = {}
        for index,letter in enumerate(alphabet):
            alphabetIndex[letter] = index
        
        change = [0]*N
        
        #prepare the shift [start,end, direction], based on direction from start add and from one passed end substract
        
        for shift in shifts:
            if shift[2]:
                change[shift[0]] += 1
                if shift[1] != N-1:
                    change[shift[1]+1] -= 1
            else:
                change[shift[0]] -= 1
                if shift[1] != N-1:
                    change[shift[1]+1] += 1
        
        #prefix sum add
        for i in range(1,N):
            change[i] += change[i-1]
        
        #alphabet index plus the change then if passed 26 modulo to circle back
        for i in range(N):
            change[i] = alphabet[(change[i]+alphabetIndex[s[i]])%26]
        

        return ''.join(change)
        
        