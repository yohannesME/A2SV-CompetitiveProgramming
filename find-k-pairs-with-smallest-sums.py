class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for num1 in nums1:
             for num2 in nums2:
                if len(heap) < k:
                    heappush(heap,[-num1-num2, num1, num2])
                elif heap[0] < [-num1-num2, num1, num2]:
                    heapreplace(heap,[-num1-num2, num1, num2])
                else:
                    break

        return [[a, b] for _ , a,b in heap]