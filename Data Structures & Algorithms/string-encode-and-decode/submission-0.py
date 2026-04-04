class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) +"#"+s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        len_sub_s = ""
        idx =0
        res =[]
        while idx < len(s):
            while s[idx] != "#":
                len_sub_s +=s[idx]
                idx+=1
            idx+=1
            len_sub_s_int = int(len_sub_s)
            res.append(s[idx:(idx+len_sub_s_int)])
            idx += len_sub_s_int
            len_sub_s = ""
        return res
