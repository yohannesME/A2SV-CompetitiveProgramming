class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([amount])
        visited = set([amount])

        coinsUsed = 0
        while queue:
            for i in range(len(queue)):
                amt = queue.popleft()

                if amount < 0:
                    continue
                
                if amt == 0:
                    return coinsUsed

                for coin in coins:
                    val = amt - coin
                    if val > 0 and val not in visited:
                        queue.append(val)
                        visited.add(val)
                    if val == 0:
                        return coinsUsed + 1
            coinsUsed += 1
        return -1