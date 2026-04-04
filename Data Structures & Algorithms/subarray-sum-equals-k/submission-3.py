class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        ans = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in prefix_sum:
                ans += prefix_sum[s-k]
            prefix_sum[s] += 1
        
        return ans
