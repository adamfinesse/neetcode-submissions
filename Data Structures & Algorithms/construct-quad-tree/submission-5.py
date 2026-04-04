"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row_start,row_end,col_start,col_end):
            val = grid[row_start][col_start]
            node = Node(val,True)
            for r in range(row_start,row_end):
                for c in range(col_start,col_end):
                    if grid[r][c] != val:
                        node.isLeaf = False
                        node.topLeft = dfs(row_start, (row_start+row_end)//2,col_start,(col_start+col_end)//2)
                        node.topRight = dfs(row_start, (row_start+row_end)//2, (col_start+col_end)//2, col_end)
                        node.bottomLeft = dfs((row_start+row_end)//2,row_end,col_start, (col_start+col_end)//2)
                        node.bottomRight = dfs((row_start+row_end)//2,row_end,(col_start+col_end)//2, col_end)
                        return node

            return node
        
        ROWS,COLS = len(grid),len(grid)

        return dfs(0,ROWS,0,COLS)


              