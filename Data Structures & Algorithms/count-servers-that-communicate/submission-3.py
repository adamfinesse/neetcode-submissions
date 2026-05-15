class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        r_cnt = [0]* len(grid)
        for r in range(len(grid)):
            servers_in_row = 0
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    servers_in_row +=1
            if servers_in_row > 1:
                r_cnt[r] += servers_in_row

        c_cnt = [0]* len(grid[0])
        for c in range(len(grid[0])):
            servers_in_col = 0
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    servers_in_col +=1
            if servers_in_col > 1:
                c_cnt[c] += servers_in_col
        
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r_cnt[r] or c_cnt[c]):
                    total+=1
        return total

        
            
