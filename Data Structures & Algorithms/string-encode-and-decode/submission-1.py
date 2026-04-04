class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i <len(s):
            if s[i] == "#":
                length = int(s[j:i])
                res.append(s[i+1:i+length+1])
                j =i+length+1
                i = i+length
            i+=1
        return res
