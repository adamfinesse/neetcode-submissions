class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0

        res = []
        def backtrack(arr,i):
            if i >= len(nums):
                nonlocal xor_sum
                tmp = 0
                for i in res:
                    tmp ^= i
                xor_sum += tmp
                return
            
            res.append(nums[i])
            backtrack(res,i+1)
            res.pop()
            backtrack(res,i+1)
        backtrack(res,0)
        return xor_sum
