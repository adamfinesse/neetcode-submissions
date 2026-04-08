class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        def dfs(r,c,s,prev):
            if r<0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in s:
                return
        
            if heights[r][c] >= prev:
                s.add((r,c))
                dfs(r+1,c,s,heights[r][c])
                dfs(r,c+1,s,heights[r][c])
                dfs(r,c-1,s,heights[r][c])
                dfs(r-1,c,s,heights[r][c])
            return

        #loop through pacific, add all indexes that can reach the pacific to the pacific_set
        # we check equal or increasing
        for c in range(COLS):
            dfs(0, c, pacific_set, heights[0][c])
        for r in range(ROWS):
            dfs(r,0,pacific_set,heights[r][0])

        #do the same for the atlantic
        for c in range(COLS):
            dfs(ROWS-1, c, atlantic_set, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, COLS-1, atlantic_set, heights[r][COLS-1])

        #find the indicies that are in both pacific/atlantic, as these can reach both oceans
        ans = []
        for idx in pacific_set:
            if idx in atlantic_set:
                ans.append(idx)
        return ans
        