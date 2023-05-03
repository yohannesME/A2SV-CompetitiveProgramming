class Solution:
    def racecar(self, target: int) -> int:
        distance = 0
        queue = deque([(0,1)])
        visited = set([(0,1)])

        while queue:
            # print(len(queue))
            for _ in range(len(queue)):
                position, speed = queue.popleft()
                
                if position == target:
                    return distance
                
                if position + speed == target:
                    return distance + 1

                #Position if i took take 'A'
                A = (position+speed, speed*2)


                if A not in visited and A[0] > 0 and A[0] < (target << 1) :
                    queue.append(A)
                    visited.add(A)

                # Position if i took 'B'
                if speed > 0:
                    speed = -1
                else:
                    speed = 1

                B = (position, speed)
                
                if B not in visited and B[0] > 0 and B[0] < (target << 1):
                    queue.append(B)
                    visited.add(B)

            distance += 1
        return -1