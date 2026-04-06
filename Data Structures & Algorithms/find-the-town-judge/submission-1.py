class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1
        count = [trust[0][1],1]

        for i in range(1,len(trust)):
            if trust[i][1] != count[0]:
                return -1
            count[1] += 1
        return count[0] if count[1] == n-1 else -1

