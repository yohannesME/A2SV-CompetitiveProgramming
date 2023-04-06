class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        multiplied = 1
        for num in nums:
            multiplied *= num
        
        def factor(n: int) -> list[int]:
            factorization: list[int] = []
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)
            
            return factorization

        primes = set()
        for num in nums:
            primes.update(factor(num))

        return len(primes)