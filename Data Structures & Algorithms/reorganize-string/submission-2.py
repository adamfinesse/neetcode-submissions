from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)

        heap = [(count,char) for char,count in char_counts.items()]
        heapq.heapify_max(heap)

        cooldown = None
        res = ""

        while heap:
            count,char = heapq.heappop_max(heap)

            if res and res[-1] == char:
                return ""
            res += char

            if cooldown:
                heapq.heappush_max(heap,cooldown)
                cooldown = None

            if count-1 >0:
                cooldown = (count-1,char)
            
        if cooldown:
            return ""
        return res


