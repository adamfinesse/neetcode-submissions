class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr,i):
            if i == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[i])
            backtrack(arr,i+1)
            arr.pop()
            backtrack(arr,i+1)
        backtrack([],0)
        return res
