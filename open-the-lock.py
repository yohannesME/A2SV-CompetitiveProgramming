class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #convert string to the tuple value of numbers
        def convert(val):
            return tuple(map(int, [*val])) 

        #the dead ends are the values we can not persue no more hence visited already in the BFS Graph.
        visited = set(list(map(convert, deadends)))
        queue = deque([(0,0,0,0)])
        target = convert(target)
        turns = 1

        #start is the target hence just return 0
        if target == (0,0,0,0):
            return 0
        
        #we can't start from the start then no need bye
        if (0,0,0,0) in visited:
            return -1

        while queue:
            for i in range(len(queue)):
                key = list(queue.popleft())
                #for each key add and substract one of the value hence check every possibility.
                for i in range(4):
                    key[i] = ((key[i]+1)%10)

                    new_val = tuple(key)
                    if new_val not in visited:
                        visited.add(new_val)
                        queue.append(new_val)
                    
                    if new_val == target:
                        return turns

                    key[i] = ((key[i]-2)%10)
                    

                    new_val = tuple(key)
                    if new_val not in visited:
                        visited.add(new_val)
                        queue.append(new_val)
                    
                    if new_val == target:
                        return turns
                    key[i] = ((key[i]+1)%10)

            turns += 1

        return -1