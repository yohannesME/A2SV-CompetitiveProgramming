class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = rooms[0][:]
        visited = set([0])

        while queue:
            room = queue.pop()
    
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
            visited.add(room)
                        
        return len(rooms) == len(visited)