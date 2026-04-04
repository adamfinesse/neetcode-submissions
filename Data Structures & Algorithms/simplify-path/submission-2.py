class Solution:
    def simplifyPath(self, path: str) -> str:
        s= []

        i=0
        while i <len(path):
            if path[i]== "/":
                i+=1
                continue
            tmp = "/"
            while i<len(path) and path[i] != "/":
                tmp+=path[i]
                i+=1
            if tmp== "/..":
                if s:
                    s.pop()
            elif tmp != "/.":
                s.append(tmp)

        return "".join(s) if s else "/"
            