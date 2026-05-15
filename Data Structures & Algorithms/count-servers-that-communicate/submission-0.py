class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        starts = []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    starts.append((r,c))
        
        visited = set()
        servers = set()

        for r,c in starts:
            high_r = 0
            while high_r < len(grid):
                if grid[high_r][c] == 1 and (high_r,c) not in servers and (high_r,c) != (r,c): 
                    servers.add((high_r,c))
                    if (r,c) not in servers:
                        servers.add((r,c))
                high_r+=1
            
            high_c = 0
            while high_c < len(grid[r]):
                if grid[r][high_c] == 1 and (r,high_c) not in servers and (r,high_c) != (r,c): 
                    servers.add((r,high_c))
                    if (r,c) not in servers:
                        servers.add((r,c))
                high_c+=1
                
        return len(servers)

            
