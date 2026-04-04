class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""

        i1=0
        i2=0
        while i1 < len(word1) and i2 < len(word2):
            s+= word1[i1] + word2[i2]
            i1+=1
            i2+=1
        if i1 <len(word1):
            s+= word1[i1:] 
        if i2 <len(word2):
            s+= word2[i2:] 
        return s