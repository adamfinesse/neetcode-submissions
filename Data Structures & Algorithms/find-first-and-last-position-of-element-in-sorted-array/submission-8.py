class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1

        potential_left = -1
        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                potential_left = m
                r = m-1
            elif nums[m] > target or (nums[m] == target and m != 0 and nums[m-1] == target):
                r = m-1
            else:
                l = m+1
        
        l,r = 0,len(nums)-1    
        potential_right = -1
        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                potential_right = m
                l = m+1

            elif nums[m] > target:
                r = m-1
            else:
                l = m+1

        return [potential_left,potential_right]