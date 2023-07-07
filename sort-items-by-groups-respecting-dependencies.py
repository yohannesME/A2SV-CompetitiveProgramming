class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def topoSort(nodes, adjList, indegree):
            queue = deque()

            for n in nodes:
                if n not in indegree:
                    queue.append(n)
            
            ordered = []

            while queue:
                node = queue.popleft()
                ordered.append(node)

                for child in adjList[node]:
                    indegree[child] -= 1

                    if indegree[child] == 0:
                        queue.append(child)
            
            return ordered
        
        group_items = defaultdict(list)
        groupId = m

        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1

            group_items[group[i]].append(i)

        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    item_graph[u].append(v)
                    item_indegree[v] += 1

        sorted_group_items = {}

        for groupId in group_items:
            sorted_items = topoSort(group_items[groupId], item_graph, item_indegree)

            if len(sorted_items) != len(group_items[groupId]):
                return []
            
            sorted_group_items[groupId] = sorted_items
        
        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1          
        
        groups = set(group)

        sorted_groups = topoSort(groups, group_graph, group_indegree)

        if len(groups) != len(sorted_groups):
            return []
        
        answer = []

        for groupId in sorted_groups:
            answer.extend(sorted_group_items[groupId])

        return answer