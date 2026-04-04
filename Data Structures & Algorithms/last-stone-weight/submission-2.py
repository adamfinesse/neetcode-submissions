class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            y = s1-s2
            if y > 0:
                heapq.heappush_max(stones,y)
        return heapq.heappop_max(stones) if stones else 0