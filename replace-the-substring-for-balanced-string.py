class Solution:
    def balancedString(self, s: str) -> int:
        shash = Counter(s)
        N = len(s)
        portion = N//4
        window = N

        left = 0
        for right, char in enumerate(s):

            shash[char]-=1
            count = sum(value <= portion for value in shash.values())

            if count == len(shash):
                while left <= right and  shash[s[left]] < portion:
                    window = min(window, right-left+1)
                    shash[s[left]] += 1
                    left += 1
                window = min(window, right-left+1)

        return window