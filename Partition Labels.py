class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexHash = {}
        output = []
        N = len(s)
        
        for i in range(N):
            lastIndexHash[s[i]] = i
        
        l,r = 0,N-1
        
        while l < N:
            if l < lastIndexHash[s[l]]:
                r = lastIndexHash[s[l]]
                start = l
                while l != r:
                    l += 1
                    r = max(r, lastIndexHash[s[l]])
                output.append(r-start+1)
            else:
                output.append(1)
                
            l += 1
        return output
