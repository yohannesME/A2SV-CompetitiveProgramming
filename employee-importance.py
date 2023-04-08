"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #create adjacecy list from the given list of employees
        adjList = defaultdict(Employee)

        for employee in employees:
            adjList[employee.id] = employee
        
        #take the id and traverse the graph using dfs
        def dfs(node, visited=set()):
            #if not visited traverse and gather the importance
            if node in visited:
                return 0
            
            visited.add(node)
            importance = adjList[node].importance

            #check for all the subordinates
            for employee in adjList[node].subordinates:
                importance += dfs(employee, visited)
            
            return importance
        
        return dfs(id)