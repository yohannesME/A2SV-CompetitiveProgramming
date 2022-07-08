class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str1 = [str(num) for num in nums]
        def sortCompare(n1,n2):
            if n1+n2 < n2+n1:
                return -1
            else:
                return 1
        str1.sort(key = cmp_to_key(sortCompare), reverse=True)

        return str(int(''.join(str1)))
