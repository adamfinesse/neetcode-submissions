class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)

        l,r=0,0
        sub_len = 0
        while l < len(s) and r < len(s):
            counts[s[r]] +=1
            while counts[s[r]] > 1:
                counts[s[l]]-=1
                l+=1
            r+=1
            sub_len = max(r-l,sub_len)
        return sub_len
