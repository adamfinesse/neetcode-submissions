class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        indicies = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    indicies.add((r,c))
        
        def update(r,c):            
            for rr in range(len(matrix)):
                matrix[rr][c] = 0
            for cc in range(len(matrix[0])):
                matrix[r][cc] = 0
            
        for r,c in indicies:
            update(r,c)
        
        