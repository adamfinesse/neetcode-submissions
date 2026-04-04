class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        ans = []

        for k,v in counts.items():
            if v > (len(nums)//3):
                ans.append(k)
        return ans