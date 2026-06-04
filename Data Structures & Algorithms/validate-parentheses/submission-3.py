class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if not stack and bracket in (")","]","}"):
                return False
            elif (bracket == ")" and stack[-1] == "("
                    or bracket == "]" and stack[-1] == "["
                    or bracket == "}" and stack[-1] == "{"):
                stack.pop()
            else:
                stack.append(bracket)
        
        return not stack