class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = len(arr)
        left = 0
        right = N-1

        while left < right:
            mid = (left+right)//2

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid

        if arr[right] - right - 1 < k:
            return  k  + right + 1
        else:
            if right == 0:
                return k
            else:
                return arr[right-1] + k - (arr[right-1] - right )