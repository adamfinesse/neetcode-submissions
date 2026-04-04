class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k= len(nums)

        j = 0
        i=0
        while i <len(nums):
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
                k-=1

            nums[j] = nums[i]
            i+=1
            j+=1
        return k
                