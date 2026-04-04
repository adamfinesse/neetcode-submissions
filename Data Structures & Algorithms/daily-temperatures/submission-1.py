class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        s = []

        for i,v in enumerate(temperatures):
            while s and v > s[-1][0]:
                _v,temp_i = s.pop()
                res[temp_i] = i-temp_i
            s.append([v,i])
        return res