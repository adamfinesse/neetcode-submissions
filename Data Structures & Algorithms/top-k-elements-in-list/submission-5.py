class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        h = [[] for i in range(len(nums)+1)]
       
        for key,val in freqs.items():
            h[val].append(key)
        
        ans = []
        for i in range(len(h)-1,-1,-1):
            while h[i] and k:
                ans.append(h[i].pop())
                k-=1
        return ans
        
