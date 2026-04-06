class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r,c))
            return 1 + (
                dfs(r+1,c) +
                dfs(r-1,c) +
                dfs(r,c+1) +
                dfs(r,c-1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c] == 1:
                    max_area = max(dfs(r,c),max_area)
        return max_area