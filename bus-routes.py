class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adjList = defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                adjList[stop].add(i)

        print(adjList)

        answer = 0

        queue = deque([source])

        seen_stop = set()
        seen_route = set()

        while queue:
            for _ in range(len(queue)):
                current_stop = queue.popleft()

                if current_stop == target:
                    return answer
                
                for route_index in adjList[current_stop]:
                    if route_index not in seen_route:
                        for stop in routes[route_index]:
                            queue.append(stop)
                            seen_stop.add(stop)
                        seen_route.add(route_index)
                
            answer += 1
        return -1