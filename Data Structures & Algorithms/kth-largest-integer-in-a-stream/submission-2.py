class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_len = k
        self.heap = []
        for n in nums:
            if len(self.heap) == k:
                heapq.heappushpop(self.heap,n)
            else:
                heapq.heappush(self.heap,n)

    def add(self, val: int) -> int:
        if len(self.heap) == self.heap_len:
            heapq.heappushpop(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
        return self.heap[0]
        
