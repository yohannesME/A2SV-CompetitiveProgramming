class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0]

        for bill in bills:
            if change[0] < 0 or change[1] < 0:
                return False

            if bill == 5:
                change[0] += 1
            elif bill == 10:
                change[1] += 1
                change[0] -= 1
            else:
                change[0] -= 1
                if change[1] == 0:
                    change[0] -= 2
                else:
                    change[1] -= 1

        if change[0] < 0 or change[1] < 0:
            return False

        return True