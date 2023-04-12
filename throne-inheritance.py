class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isAlive = True

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.royalFamily = TreeNode(kingName)
        self.memo = defaultdict(TreeNode)
        self.memo[kingName] = self.royalFamily

    #get a node by traversing and return it
    def dfs(self,root, nodeName):
        if root.name == nodeName:
            return root

        
        for children in root.children:
            node = self.dfs(children, nodeName)
            if node:
                return node
                

    #get the parent and add it as a child for that parent 
    def birth(self, parentName: str, childName: str) -> None:
        child = TreeNode(childName)
        self.memo[childName] = child
        self.memo[parentName].children.append(child)

    #mark the isAlive Flag False for that node
    def death(self, name: str) -> None:
        self.memo[name].isAlive = False

    #Generate all successors if they are alive
    def getInheritanceOrder(self) -> List[str]:
        successors = []

        def dfs(root):
            if not root:
                return 

            if root.isAlive:
                successors.append(root.name)

            for children in root.children:
                dfs(children)
        
        dfs(self.royalFamily)
        return successors


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()