class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for i in range(len(nums)):
            r = target - nums[i]
            if r in idx_map:
                return [idx_map[r],i]
            idx_map[nums[i]] = i
