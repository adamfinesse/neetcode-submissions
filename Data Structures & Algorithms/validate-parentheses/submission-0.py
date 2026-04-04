class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if stack:
                if c == "(" or c == "[" or c == "{":
                    stack.append(c)
                    continue

                paren = stack.pop()
                if (c == "]" and paren == "[") or (c ==")" and paren == "(") or (c == "}" and paren == "{"):
                    continue
                else:
                    return False
            stack.append(c)
        return not stack
                    
                    
