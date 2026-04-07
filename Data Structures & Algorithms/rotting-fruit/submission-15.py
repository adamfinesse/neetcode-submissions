from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        
        def add_cell(r,c):
            if r <0 or c < 0 or c >= COLS or r >= ROWS or (r,c) in seen or grid[r][c] == 0 or grid[r][c] == 2:
                return
            seen.add((r,c))
            q.append((r,c))
            return
        fresh = 0
        #find our starting points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    add_cell(r+1,c)
                    add_cell(r,c-1)
                    add_cell(r,c+1)
                    add_cell(r-1,c)
                elif grid[r][c] == 1:
                    fresh +=1

        # while we have potential cells to visit, keep checking
        minutes = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 1:
                    fresh -=1
                grid[r][c] = 2

                add_cell(r+1,c)
                add_cell(r,c-1)
                add_cell(r,c+1)
                add_cell(r-1,c)
            
            minutes +=1
       
        return minutes if not fresh else -1
        