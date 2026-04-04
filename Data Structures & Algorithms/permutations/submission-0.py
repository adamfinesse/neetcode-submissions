class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr,seen):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for i in range(len(nums)):
                if i in seen:
                    continue
                arr.append(nums[i])
                seen.add(i)
                backtrack(arr,seen)
                arr.pop()
                seen.remove(i)
        backtrack([],set())
        return res