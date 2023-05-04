class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #as we return the index lets add it to the task
        for index,task in enumerate(tasks):
            task.append(index)
            
        #sort the enqueue times       
        tasks.sort()
        
        #tasks to be processed
        task = []
        #answer
        answer = []
        
        heapq.heapify(task)
        
        #keep track of the current time
        time = tasks[0][0]
        #processed tasks
        index = 0
        
        while index < len(tasks):
 
            
            for i in range(index,len(tasks)):
                if tasks[i][0] <= time:
                    task.append([tasks[i][1], tasks[i][2]])
                    index += 1
                else:
                    break
            if len(task) > 0:
                heapq.heapify(task)
                t = heapq.heappop(task)
                time += t[0]
                answer.append(t[1])
            else:
                time = tasks[index][0]
        
        if len(task) > 0:
            heapq.heapify(task)
            for _ in range(len(task)):
                t = heapq.heappop(task)
                time += t[0]
                answer.append(t[1])                

        
        print(task, time, tasks)
        return answer