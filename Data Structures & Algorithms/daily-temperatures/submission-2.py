class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        res = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while mono_stack and mono_stack[-1][0] < temp:
                _, stack_i = mono_stack.pop()
                res[stack_i] = i-stack_i

            mono_stack.append((temp,i))
        
        return res