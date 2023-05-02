# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #if no distance just return the target to be the element
        if k == 0:
            return [target.val]
        
        #let's change the tree to a graph
        adjList = defaultdict(list)
        def treeToGraph(root):
            if root.left:
                adjList[root.left.val].append(root.val)
                adjList[root.val].append(root.left.val)
                treeToGraph(root.left)
            
            if root.right:
                adjList[root.right.val].append(root.val)
                adjList[root.val].append(root.right.val)
                treeToGraph(root.right)
        
        treeToGraph(root)
        
        #NOW LET'S USE BFS TO FIND THE KTH DISTANCE ELEMENTS
        queue = deque([target.val])
        visited = set([target.val])
        for _ in range(k):
            for _ in range(len(queue)):
                node = queue.popleft()

                for child in adjList[node]:
                    if child in visited:
                        continue
                    
                    visited.add(child)
                    queue.append(child)
        
        return list(queue)