class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        h= []
        for key,v in freqs.items():
            h.append((v,key))
        heapq.heapify_max(h)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop_max(h)[1])
        return ans
        
