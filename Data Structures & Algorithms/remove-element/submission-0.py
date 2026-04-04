class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)-1
        i=0

        while i<=k:
            if nums[i] == val:
                nums[i],nums[k] = nums[k], nums[i]
                k-=1
                i-=1
            i+=1
        return k+1