class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        lagging = 0
        fast = 1
        for i in range(n-1):
            fast += lagging
            lagging = fast - lagging
        return fast
        