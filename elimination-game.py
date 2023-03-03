# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         def eliminate(left, right, iteration, isRight):
#             if left == right:
#                 return right
#             else:
#                 length = (right-left)//iteration
#                 length += 1
#                 if length%2 == 0:
#                     if isRight:
#                         right -= iteration
#                     else:
#                         left += iteration
#                 else:
#                     right -= iteration
#                     left += iteration

#                 return eliminate(left, right, iteration*2, not isRight)
        
#         return eliminate(1,n, 1, False)


class Solution:
    def lastRemaining(self, n: int) -> int:
        def eliminate(left, length, iteration, isRight):
            if length == 1:
                return left
            else:
                if length%2 == 0:
                    if not isRight:
                        left += iteration
                else:
                    left += iteration

                return eliminate(left, length//2, iteration*2, not isRight)
        
        return eliminate(1, n, 1, False)