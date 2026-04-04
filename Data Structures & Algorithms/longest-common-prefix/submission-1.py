class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        lcp_idx=0
        while True:
            if lcp_idx >= len(strs[0]):
                return lcp 
            temp_lcp = strs[0][lcp_idx]
            for i in range(1,len(strs)):
                if lcp_idx >= len(strs[i]) or temp_lcp != strs[i][lcp_idx]:
                    return lcp
            lcp += temp_lcp
            lcp_idx +=1




