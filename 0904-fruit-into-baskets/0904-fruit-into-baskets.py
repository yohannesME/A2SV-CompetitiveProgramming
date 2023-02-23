class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        basket = defaultdict(int)
        total = 0
        start = 0
        end = 0
        
        while end < len(fruits):
            #add to the basket until it is full
            while end < len(fruits):
                basket[fruits[end]] += 1
                if len(basket) > 2:
                    basket.pop(fruits[end])
                    break
                end += 1
                
            #then update the total and remove from the back and fill it back again
            total = max(total, sum(list(basket.values())))
            basket[fruits[start]] -= 1
            
            #if empty then pop
            if basket[fruits[start]] == 0:
                basket.pop(fruits[start])
            start += 1
        
        return total
            
