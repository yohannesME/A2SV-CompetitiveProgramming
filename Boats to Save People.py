class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        total = 0
        while l <= r:
            if l == r:
                total += 1
                break
            if people[l] == limit:
                total += 1
                l+=1
            if people[r] == limit:
                total += 1
                r-=1
            if people[r] + people[l] <= limit:
                total += 1
                l += 1
                r -= 1
            else:
                r -= 1
                total += 1
        return total
