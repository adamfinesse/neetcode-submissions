class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        def backtrack(arr,i):
            if i == len(nums):
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(arr,i+1)
            arr.pop()
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(arr,i+1)
            
        backtrack([],0)
        return res
