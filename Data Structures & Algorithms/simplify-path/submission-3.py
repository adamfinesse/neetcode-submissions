class Solution:
    def simplifyPath(self, path: str) -> str:
        s= []
        print(path.split("/"))
        path = path.split("/")

        for p in path:
            if p == "..":
                if s:
                    s.pop()
            elif p == "." or not p:
                continue
            else:
                s.append(f"/{p}")
        return "".join(s) if s else "/"
        