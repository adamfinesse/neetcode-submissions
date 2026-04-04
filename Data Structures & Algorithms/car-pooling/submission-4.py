class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        
        heap = []
        km = trips[0][1]
        i=0
        while i < len(trips):
            while heap and heap[0][0] == km:
                dropoff,ppl = heapq.heappop(heap)
                capacity += ppl

            ppl, pickup, dropoff = trips[i]
            if capacity < ppl and pickup <= km:
                return False
            if capacity >= ppl:
                capacity -= ppl
                heapq.heappush(heap,(dropoff,ppl))
                i+=1
            km+=1
        return True
