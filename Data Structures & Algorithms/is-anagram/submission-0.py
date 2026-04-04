class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        return t==s