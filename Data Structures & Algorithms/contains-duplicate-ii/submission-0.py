class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in dups and abs(dups[nums[i]]-i) <=k:
                return True
            dups[nums[i]]=i
        return False