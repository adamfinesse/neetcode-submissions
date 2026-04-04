class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(arr,open,closed):
            if open == n and closed == n:
                res.append("".join(arr))
                return
            
            if open > closed:
                arr.append(")")
                backtrack(arr,open,closed+1)
                arr.pop()

            if open < n:
                arr.append("(")
                backtrack(arr,open+1,closed)
                arr.pop()
        backtrack([],0,0)
        return res
            
