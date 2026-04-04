class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(arr,i,running_sum):
            if running_sum >= target or i == len(nums):
                if running_sum == target:
                    res.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(arr,i,running_sum+nums[i])
            arr.pop()
            backtrack(arr,i+1,running_sum)
        backtrack([],0,0)
        return res