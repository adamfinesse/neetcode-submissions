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

            tmp = []
            if not prev or prev[0] < cnt:
                while cnt and len(tmp) < 2:
                    tmp.append(char)
                    cnt-=1
            else:
                tmp.append(char)
                cnt-=1
            
            res.append("".join(tmp))
            if prev:
                heapq.heappush_max(heap,prev)
                prev = None
            if cnt:
                prev = (cnt,char)
    
        return "".join(res)

                
