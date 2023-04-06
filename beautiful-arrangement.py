class Solution:
    def countArrangement(self, n: int) -> int:
        answer = 0

        def backtrack(num=1, mask=0):
            nonlocal answer

            if mask == 2**n-1:
                answer += 1
                return
            
            for i in range(1, n+1):
                if( i%num == 0 or num%i == 0) and mask &(1 << (n-i) ) == 0:
                    mask |= (1 << (n-i))
                    backtrack(num+1, mask)
                    mask &= ~(1 <<(n- i))

        backtrack()
        return answer