class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        task_count = defaultdict(int)

        for task in tasks:
            cycle = task_count[task]
            heapq.heappush(heap,(cycle,task))
            task_count[task] +=n+1
        
        cycles = 0
        while heap:
            if cycles >= heap[0][0]:
                heapq.heappop(heap)
            cycles+=1
        return cycles