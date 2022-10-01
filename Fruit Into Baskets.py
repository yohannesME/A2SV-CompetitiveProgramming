class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        basket = defaultdict(lambda:0, basket)
        total = 0
        start, end = 0,0
        while end < len(fruits):
            while end < len(fruits):
                basket[fruits[end]] += 1
                if len(basket) > 2:
                    basket.pop(fruits[end])
                    break
                end += 1
            total = max(total, sum(list(basket.values())))
            basket[fruits[start]] -= 1
            
            if basket[fruits[start]] == 0:
                basket.pop(fruits[start])
            start += 1
        return total
            
