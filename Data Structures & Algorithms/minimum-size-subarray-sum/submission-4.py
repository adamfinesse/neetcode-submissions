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
                while subSum > target and subSum - nums[l] >= target:
                    subSum -= nums[l]
                    l+=1
                    min_len = min(min_len, r-l)

        if min_len == 100001:
            return 0
        else:
            return min_len




