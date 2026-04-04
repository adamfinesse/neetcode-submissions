class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        
        heap = []
        for ppl, pickup, dropoff in trips:
            
            while heap and heap[0][0] <= pickup:
                d,p = heapq.heappop(heap)
                capacity += p

            capacity -= ppl
            if capacity < 0:
                    return False
        
            heapq.heappush(heap,(dropoff,ppl))
        return True
