class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r = 0,0

        max_ones = 0
        while r < len(nums):
            if nums[r] == 1:
                r+=1
                max_ones = max(max_ones,r-l)
            else:
                l = r
                l+=1
                r+=1
        return max_ones