class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s[0] != " ":
            return 1
        idx = len(s)-1
        while s[idx] == " ":
            idx -=1

        start = idx
        while s[idx] != " " and idx > 0:
            idx-=1
        return start-idx
        