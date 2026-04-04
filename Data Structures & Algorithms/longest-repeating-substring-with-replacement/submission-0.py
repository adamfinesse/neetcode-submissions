class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_len = 0
        l=0
        most_freq = 0
        for r in range(len(s)):
            if freqs.get(s[r]):
                freqs[s[r]]+=1
            else:
                freqs[s[r]]=1
            most_freq = max(freqs.values())
            r+=1
            while (r-l) - most_freq > k:
                freqs[s[l]]-=1
                l+=1
                most_freq = max(freqs.values())
            max_len = max(max_len,r-l)
        return max_len
            


