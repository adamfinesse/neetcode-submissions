class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1,len(asteroids)):
            if not stack or (asteroids[i] > 0 and stack[-1] >0)  or (asteroids[i] < 0 and stack[-1] < 0) or (asteroids[i] >0 and stack[-1] <0):
                stack.append(asteroids[i])
            elif asteroids[i] <0 and stack[-1] > 0:
                if abs(asteroids[i]) - abs(stack[-1]) == 0:
                    stack.pop()
                elif abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                    stack.append(asteroids[i])
                
                    while len(stack) >=2:
                        if (stack[-2] >0 and stack[-1] > 0) or (asteroids[-2] < 0 and stack[-1] < 0) or (stack[-2] <0 and stack[-1] > 0):
                            break
                        elif stack[-2] >0 and stack[-1] < 0:
                            if abs(stack[-2]) - abs(stack[-1]) == 0:
                                stack.pop()
                                stack.pop()
                            elif abs(stack[-2]) > abs(stack[-1]):
                                stack.pop()
                            elif abs(stack[-2]) < abs(stack[-1]):
                                stack.pop(-2)
                        else:
                            break
                            

        return stack