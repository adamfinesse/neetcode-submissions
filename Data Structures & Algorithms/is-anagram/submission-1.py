class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ans = [0]* 26

        for i in range(len(s)):
            ans[ord(s[i])- ord('a')] += 1
            ans[ord(t[i])- ord('a')]  -= 1

        for n in ans:
            if n != 0:
                return False
        return True
        