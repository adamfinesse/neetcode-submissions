class Solution:
    def solve(self, board: List[List[str]]) -> None:
        grid = board
        seen = set()
        ROWS = len(board)
        COLS = len(board[0])

       
        def check_connected(r,c):
            if r <0 or c <0 or r>= ROWS or c >= COLS or grid[r][c] == "X" or (r,c) in seen:
                return
            seen.add((r,c))
            check_connected(r-1,c)
            check_connected(r+1,c)
            check_connected(r,c+1)
            check_connected(r,c-1)
            
        for r in range(ROWS):
            if grid[r][0] == "O":
                check_connected(r,0)
            if grid[r][COLS-1] == "O":
                check_connected(r,COLS-1)
        for c in range(COLS):
            if grid[0][c] == "O":
                check_connected(0,c)
            if grid[ROWS-1][c] == "O":
                check_connected(ROWS-1,c)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "O" and (r,c) not in seen:
                    grid[r][c] = "X"

                    