class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c = {}
        s2_c = {}
        for c in s1:
            if s1_c.get(c):
                s1_c[c] +=1
            else:
                s1_c[c] = 1
        
        l=0
        for r in range(len(s2)):
            if s2[r] in s1_c:
                if s2_c.get(s2[r]):
                    s2_c[s2[r]]+=1
                else:
                    s2_c[s2[r]] = 1
                while s2_c[s2[r]] > s1_c[s2[r]]:
                    s2_c[s2[l]] -=1
                    l+=1
                if s1_c == s2_c:
                    return True
            elif s2[r] not in s1_c:
                while l<r:
                    s2_c[s2[l]] -=1
                    l+=1
                l+=1
            else:
                l=r+1
        return False
