class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(i,arr,total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target or i == len(candidates):
                return
            
            arr.append(candidates[i])
            backtrack(i+1,arr,total+candidates[i])
            arr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,arr,total)
        backtrack(0,[],0)
        return res