class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        result = 0
        
        while (l < r):
            result = max(result, (r-l)*min(height[r],height[l]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result
