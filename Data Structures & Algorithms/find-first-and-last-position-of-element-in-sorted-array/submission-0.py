class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1

        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                while nums[l] != target:
                    l+=1
                while nums[r] != target:
                    r-=1
                return [l,r]
            
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
        
        return [-1,-1]