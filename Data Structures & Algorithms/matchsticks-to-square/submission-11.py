class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size = sum(matchsticks)

        if size % 4 != 0:
            return False

        partition_arr = [0]*4
        partition = size//4
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i >= len(matchsticks):
                return True

            for j in range(len(partition_arr)):
                if partition_arr[j] + matchsticks[i] <= partition:
                    partition_arr[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    partition_arr[j] -= matchsticks[i]
            return False
        return backtrack(0)
             
            