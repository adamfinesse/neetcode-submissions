class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        stack = []

        for i in range(len(s)):
            if stack and s[i] == ")":
                stack.pop()
            elif not stack and star_stack and star_stack[-1] < i and s[i] == ")":
                star_stack.pop()
            elif s[i] == "*":
                star_stack.append(i)
            elif s[i] == "(":
                stack.append(i)
            else:
                return False

        while stack and star_stack:
            if star_stack[-1] < stack[-1]:
                return False
            star_stack.pop()
            stack.pop()

        return not stack
            