class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_len = 0
        l=0
        for r in range(len(s)):
            if freqs.get(s[r]):
                freqs[s[r]]+=1
            else:
                freqs[s[r]]=1

            while (r-l+1) - max(freqs.values()) > k:
                freqs[s[l]]-=1
                l+=1

            max_len = max(max_len,r-l+1)
        return max_len
            


