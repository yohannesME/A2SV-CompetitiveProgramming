class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        # @functools.cache
        def playerWinner(left, right, player1Turn, memo={}):
            print(memo)
            #base case when there is left only one element return it to the player in which it is the turn
            if left == right:
                if player1Turn:
                    return [nums[left],0]
                else:
                    return [0, nums[right]]
            else:
                #the recurrence - check whose turn ask for the result from the two possible path tooken and compare which will be more optimal and traverse with that direction.
                #added the memo
                
                if (left+1, right, player1Turn) in memo:
                    resultLeft = memo[(left+1, right, player1Turn)][:]
                else:
                    resultLeft = playerWinner(left+1, right, not player1Turn, memo)
                    memo[(left+1, right, player1Turn)] = resultLeft[:]

                if (left, right-1, player1Turn) in memo:
                    resultRight = memo[(left, right-1)][:]
                else:
                    resultRight = playerWinner(left, right-1, not player1Turn, memo)
                    memo[(left, right-1, player1Turn)] = resultRight[:]

                if player1Turn:
                    resultLeft[0] += nums[left]
                    resultRight[0] += nums[right]
                    if resultLeft[0] > resultRight[0]:
                        return resultLeft
                    else:
                        return resultRight
                else:
                    resultLeft[1] += nums[left]
                    resultRight[1] += nums[right]
                    if resultLeft[1] > resultRight[1]:
                        return resultLeft
                    else:
                        return resultRight
        
        #our function return the score and just check which one is greater.
        score = playerWinner(0, len(nums)-1, True)
        return score[0] >= score[1]



        # def checkWinner(nums, player1, player2, turnPlayer1):
        #     if len(nums) == 0:
        #         return [0,0]
        #     else:
        #         if turnPlayer1:
        #             return checkWinner(nums[1:], player1+nums[0], player2, not turnPlayer1) or checkWinner(nums[:-1], player1+nums[-1], player2, not turnPlayer1)
        #         else:
        #             if len(nums) > 1:
        #                 if nums[0] >= nums[-1]:
        #                     return checkWinner(nums[1:], player1, player2+nums[0], not turnPlayer1)
        #                 else:
        #                     return checkWinner(nums[:-1], player1, player2+nums[-1], not turnPlayer1)
        #             else:
        #                 return checkWinner(nums[1:], player1, player2+nums[0], not turnPlayer1)
        
        # return checkWinner(nums, 0,0,True)