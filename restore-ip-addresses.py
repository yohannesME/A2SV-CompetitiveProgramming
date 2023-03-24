class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        s= list(s)
        N = len(s)
        output = []


        def backtrack(currentIp=[], index=0):
            #if we reach three accumulated ip partition what is left is the last one so just validate the formed ip and append it
            if len(currentIp) == 3:
                lastpart = ''.join(s[index:])

                if ((len(lastpart) > 1 and lastpart[0] != '0') or len(lastpart) == 1 ) and int(lastpart) < 256:
                    newIp = []
                    for ip in currentIp:
                        newIp.append(''.join(ip))
                        if int(newIp[-1]) > 255:
                            return
                    newIp.append(lastpart)
                    output.append('.'.join(newIp))
                return
            
            #the backtracking happens using the array
            currentIp.append([])
            for i in range(index, N):
                currentIp[-1].append(s[i])
                
                #uf current ip exceeds the valid ip just break from the path
                if len(currentIp[-1]) > 3 or (len(currentIp[-1]) > 1 and currentIp[-1][0] == '0'):
                    break

                backtrack(currentIp, i+1)
            
            currentIp.pop()

        
        backtrack()
        return output