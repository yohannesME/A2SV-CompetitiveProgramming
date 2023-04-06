class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        ans = []
        primes = []
        for num in range(left, right+1):
            if isPrime(num):
                primes.append(num)
            if len(primes) > 1:

                if primes[-1] - primes[-2] <= 2:
                    return [primes[-2], primes[-1]]

                if not ans:
                    ans = [primes[-2], primes[-1]]
                elif primes[-1] - primes[-2] < ans[1]-ans[0]:
                    ans[0] = primes[-1]
                    ans[1] = primes[-2]
        if not ans:
            return [-1,-1]
        
        return ans