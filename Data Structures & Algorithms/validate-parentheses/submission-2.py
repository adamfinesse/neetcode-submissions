class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            print(stack)
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue
            elif stack:
                char = stack.pop()
                if c == ")" and char == "(" or c == "}" and char == "{" or c == "]" and char == "[":
                    continue
            return False
        return not stack