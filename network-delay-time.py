import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        graph = {}
        visited = set()

        for time in times:
            if time[0] not in graph:
                graph[time[0]] = []
            graph[time[0]].append((time[1], time[2]))

        q = [(0, k)]

        while q:
            dis, node = heapq.heappop(q)

            if node in visited:
                continue
            visited.add(node)

            if node in graph:
                for val in graph[node]:
                    if dis + val[1] < distance[val[0]]:
                        distance[val[0]] = dis + val[1]
                        heapq.heappush(q, (distance[val[0]], val[0]))

        ans = max(distance[1:])
        return ans if ans != float('inf') else -1