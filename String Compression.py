class Solution:
    def compress(self, chars: List[str]) -> int:
        cur, nex = 0,0
        result = ""

        while nex < len(chars):

            if chars[cur] == chars[nex]:
                
                while len(chars) > nex and chars[cur]==chars[nex]:
                    nex += 1
                result += (chars[cur])
                count = nex - cur
                if count > 1:
                    result += str(count) 
                cur = nex
            else:
                result += (chars[cur])
                cur += 1
                nex += 1
        for i in range(len(result)):
            chars[i] = result[i]
        
        return len(result)
