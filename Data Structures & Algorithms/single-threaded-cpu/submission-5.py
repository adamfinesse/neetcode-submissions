class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0],task[1],i) for i,task in enumerate(tasks)]

        heapq.heapify(tasks)
   
        res = []
        sub_heap = []
        c = tasks[0][0]
        while tasks or sub_heap:
            while tasks and c >= tasks[0][0]:
                task = heapq.heappop(tasks)
                heapq.heappush(sub_heap,(task[1],task[2]))

            if sub_heap:
                task = heapq.heappop(sub_heap)
                res.append(task[1])
                c += task[0]
            else:
                c=tasks[0][0]
            
            
            
        return res
