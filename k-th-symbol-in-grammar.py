class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammar(n, k):
            print(n, k)
            if n == 0:
                return False
            
            #inverted
            prevRow = pow(2, n-1)
            if k >= prevRow:
                return not grammar(n-1, k % prevRow)
            else:
                return grammar(n-1, k % prevRow)

        return 1 if grammar(n-1, k-1) else 0