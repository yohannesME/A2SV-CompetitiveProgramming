class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        #output
        completetime = 0
        
        #count of tasks of the same difficulty
        taskcounts = Counter(tasks)
        
        if 1 in taskcounts.values():
            return -1
        
        #if difficulty is divided by 3 add that but if not check if the task left are 2 if not -1
        for difficulty in taskcounts.values():
            completetime += difficulty//3 + bool(difficulty%3)

        #change the time to int as dividing will create a float
        return completetime