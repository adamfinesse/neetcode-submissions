class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        l,r = 0,0
        while r < len(s):
            if s[r].isdigit():
                stack.append(s[l:r])
                l=r
                while s[r] != "[":
                    r+=1
                stack.append(s[l:r])
                r+=1
                l=r
            elif s[r] == "[":
                stack.append(s[l:r])
                r+=1
                l=r
            elif s[r] == "]":
                tmp = s[l:r] 
                while stack and not stack[-1].isdigit():
                    tmp = stack.pop() + tmp
                tmp = tmp * int(stack.pop())
                stack.append(tmp)
                r+=1
                l=r
            else:
                r+=1
        stack.append(s[l:r])
        return "".join(stack)
                