class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""

        idx=0
        while idx < len(word1) and idx < len(word2):
            s+= word1[idx] + word2[idx]
            idx+=1

        if idx <len(word1):
            s+= word1[idx:] 
        if idx <len(word2):
            s+= word2[idx:] 
        return s