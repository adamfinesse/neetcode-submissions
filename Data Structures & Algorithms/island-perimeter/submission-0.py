class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c,seen):
            if (r,c) in seen:
                return 0
            if r < 0 or c < 0 or c > COLS-1 or r > ROWS-1 or grid[r][c] == 0:
                return 1
            if grid[r][c] == 1:
                seen.add((r,c))
                return (
                    dfs(r,c-1,seen) +
                    dfs(r,c+1,seen) +
                    dfs(r+1,c,seen) +
                    dfs(r-1,c,seen)
                )
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c,set())

        