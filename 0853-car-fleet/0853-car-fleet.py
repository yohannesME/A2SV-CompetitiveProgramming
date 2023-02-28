class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #merge the position with speed
        pair = [[p,t] for p, t in zip(position, speed)]
        
        pair.sort(reverse=True)
        
        #keep a monotonic speed
        stack = []
        for position,speed in pair:
            
            stack.append((target-position)/speed)
            
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)