class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        left = 0
        right = N-1


        while left < right:
            mid = (left + right)//2

            if citations[mid] < N-mid:
                left = mid + 1
            else:
                right = mid
        return N-left if citations[left] else 0