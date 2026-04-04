class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted = Counter(nums)

        majority=[0,0]
        for k in counted.keys():
            if counted[k] > majority[1]:
                majority = [k,counted[k]]
        return majority[0]