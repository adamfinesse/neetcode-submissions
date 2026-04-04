class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j))

        def traverse(i,j,lvl):
            if i <0 or i>= len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] == -1 or (i,j) in visited:
                return
            visited.add((i,j))

            if grid[i][j] != 0:
                grid[i][j] = lvl

            q.append((i+1,j))
            q.append((i-1,j))
            q.append((i,j+1))
            q.append((i,j-1))

        level = 0
        while q:
            for k in range(len(q)):
                i,j = q.pop(0)
                traverse(i,j,level)
            level+=1


                


