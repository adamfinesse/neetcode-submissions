class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        
        for v in counts.values():
            if v >1:
                return True
        return False

