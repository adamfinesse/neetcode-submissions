class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans= 0
        for i in num_set:
            lcs = 1
            if i-1 not in num_set:
                while i+1 in num_set:
                    lcs+=1
                    i+=1
            ans = max(lcs,ans)
        return ans
            