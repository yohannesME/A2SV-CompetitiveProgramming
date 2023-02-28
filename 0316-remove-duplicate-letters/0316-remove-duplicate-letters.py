class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        output = []
        letterHash = defaultdict(int)
        lastOccurance = {}
        N = len(s)
        
        #use to check if there is the same element twice but check forward
        for i in range(N):
            lastOccurance[s[i]] = i
        
        #when removing lexically small element we first need to check if we can find that element again 
        #when we check in the from else then we don't pop as we loose that element forever
        for index,letter in enumerate(s):

            if letterHash[letter] == 0:
                while output and output[-1] > letter and lastOccurance[output[-1]] > index:
                    letterHash[output.pop()] -= 1
            
                output.append(letter)
                letterHash[letter] += 1
                
        return ''.join(output)
                