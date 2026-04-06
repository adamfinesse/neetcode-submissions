from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c)) 
                    # if you add to seen here, we break bfs immediately
    

        level = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or grid[r][c] == -1:
                    continue
                seen.add((r,c))
                grid[r][c] = level
                q.append((r+1,c))
                q.append((r,c+1))
                q.append((r,c-1))
                q.append((r-1,c))
            level +=1
            