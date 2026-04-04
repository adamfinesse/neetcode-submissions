class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for i in range(len(nums)):
            idx_map[nums[i]] = i

        for i in range(len(nums)):
            r = target-nums[i]
            idx = idx_map.get(r,0)
            if idx and i != idx:
                return [i,idx]
        