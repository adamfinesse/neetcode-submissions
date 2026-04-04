class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s,f = nums[0], nums[0]

        while True:
            s = nums[s]
            f = nums[f]
            f = nums[f]
            if s == f:
                break
                
        s = nums[0]
        while True:
            if s == f:
                return s
            s = nums[s]
            f = nums[f]

        