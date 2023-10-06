class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][1] == s[i]:
                stack.append([stack[-1][0] + 1, s[i]])
            else:
                stack.append([1, s[i]])

            if stack and stack[-1][0] == k:
                for _ in range(k):
                    stack.pop()

        ans = []
        for i, letter in stack:
            ans.append(letter)
        return ''.join(ans)