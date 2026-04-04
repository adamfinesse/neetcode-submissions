class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0

        res = []
        def backtrack(i,total):
            if i == len(nums):
                nonlocal xor_sum
                xor_sum += total
                return
            
            res.append(nums[i])
            backtrack(i+1,total^nums[i])
            res.pop()
            backtrack(i+1,total)

        backtrack(0,0)
        return xor_sum
