class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        s = 0
        l,r=0,0

        while r< len(nums):
            s += nums[r]
            max_sum = max(max_sum,s)
            while s <0 :
                s -= nums[l]
                l+=1
            r+=1
        return max_sum
