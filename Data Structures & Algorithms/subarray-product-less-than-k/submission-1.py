from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        cnt = 0
        
        l,r = 0,0
        product = 1
        while r < len(nums):
            if nums[r] * product < k:
                product *= nums[r]
                cnt += (r - l + 1)
                r+=1
            else:
                product /= nums[l]
                l+=1
        #cnt += r-l
        return cnt