class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r-1,c))
                    q.append((r+1,c))
                    q.append((r,c-1))
                    q.append((r,c+1))
        dist = 1
        while q:
            qLen = len(q)
            for i in range(qLen):
                row,col = q.pop(0)
                if row <0 or col <0 or row >=len(grid) or col >= len(grid[row]) or grid[row][col] == -1 or grid[row][col] == 0 or (row,col) in visited:
                    continue
                if grid[row][col] > dist:
                    grid[row][col] = dist
                visited.add((row,col))
                q.append((row+1,col))
                q.append((row-1,col))
                q.append((row,col+1))
                q.append((row,col-1))
            dist+=1
                    
                    
                            

            