class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        s_to_c = {}
        c_to_s = {}

        if len(s) != len(pattern): return False

        used = set()
        i=0
        for c in pattern:
            if c in c_to_s and c_to_s[c] != s[i] or s[i] in s_to_c and s_to_c[s[i]] != c:
                return False
            if s[i] not in s_to_c and c not in c_to_s:
                s_to_c[s[i]] = c
                c_to_s[c] = s[i]
            i+=1
            
        return True
