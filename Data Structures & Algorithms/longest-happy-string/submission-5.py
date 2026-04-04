class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heap.append((a,"a"))
        if b:
            heap.append((b,"b"))
        if c:
            heap.append((c,"c"))
        heapq.heapify_max(heap)

        prev = None
        res = []
        while heap:
            cnt,char = heapq.heappop_max(heap)

            if not prev or prev[0] < cnt:
                n = 2 if cnt >= 2 else 1
                cnt -=n
                res.append(char * n)
            else:
                res.append(char)
                cnt-=1
            
            if prev:
                heapq.heappush_max(heap,prev)
                prev = None
            if cnt:
                prev = (cnt,char)
    
        return "".join(res)

                
