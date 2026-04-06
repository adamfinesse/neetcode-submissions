class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c,seen):
            if r <0 or c <0 or c >= COLS or r >= ROWS or (r,c) in seen or grid[r][c] == "0":
                return
            seen.add((r,c))

            dfs(r+1,c,seen)
            dfs(r,c+1,seen)
            dfs(r,c-1,seen)
            dfs(r-1,c,seen)

            return

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c] == "1":
                    islands+=1
                    dfs(r,c,seen)
        return islands