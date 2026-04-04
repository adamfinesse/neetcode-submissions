class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        i=0
        j=0
        decoded = []

        while i < len(s):
            if s[i] == "#":
                word_len = int(s[j:i])
                j=i+1
                i += word_len+1
                decoded.append(s[j:i])
                j=i
            i+=1
        return decoded
            
