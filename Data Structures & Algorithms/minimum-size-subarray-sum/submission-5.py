class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 100001
        subSum = 0 

        l=0
        r=0
        while r < len(nums):
                subSum += nums[r]
                r+=1
                if subSum >= target:
                    min_len = min(min_len, r-l)
                while subSum >= target:
                    min_len = min(min_len, r - l)
                    subSum -= nums[l]
                    l += 1

        return 0 if min_len == 100001 else min_len




