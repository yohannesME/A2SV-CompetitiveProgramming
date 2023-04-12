class ThroneInheritance:
    def __init__(self, kingName: str):
        self.kingName = kingName
        self.royalFamily = defaultdict(list)
        self.dead = set()            

    #get the parent and add it as a child for that parent 
    def birth(self, parentName: str, childName: str) -> None:
        self.royalFamily[parentName].append(childName)

    #add to the dead family list
    def death(self, name: str) -> None:
        self.dead.add(name)

    #Generate all successors if they are alive
    def getInheritanceOrder(self) -> List[str]:
        successors = []
        
        def dfs(node):
            if node not in self.dead:
                successors.append(node)

            for children in self.royalFamily[node]:
                dfs(children)
        
        dfs(self.kingName)
        return successors


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()