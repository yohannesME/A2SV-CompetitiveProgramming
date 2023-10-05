class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        s = str(n)
        levels = {}
        num = int('1' * len(s))

        for i in range(len(s)):
            levels[i+1] = num
            num //= 10

        levels[len(s)+1] = 0
        
        def search(start, level, k, index, countAtIndex, before , after):

            countAtIndex -= ((int(s[index]) - start) * levels[level]) + (( 10 - int(s[index])-1 ) * levels[level+1])

            for i in range(start, 10):
                if k == 1:
                    return str(i)
                if (i < int(s[index]) or before) and not after:
                    if k > levels[level]:
                        k -= levels[level]
                    else:
                        return str(i)+search(0, level+1, k-1, index+1, countAtIndex, True, False)
                elif i == int(s[index]) and not after:
                    if k > countAtIndex:
                        k -= countAtIndex
                    else:
                        return str(i)+search(0, level+1, k-1, index+1, countAtIndex-1, False, False)
                else:
                    if k > levels[level+1]:
                        k-= levels[level+1]
                    else:
                        return str(i)+search(0, level+1, k-1, index+1, countAtIndex, False, True)                        


        return int(search(1, 1, k, 0, n, False, False))