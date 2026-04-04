class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        
        for k,v in counts.items():
            if v >1:
                return True
        return False

