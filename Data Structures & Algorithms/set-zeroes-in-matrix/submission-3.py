class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def update(r,c):            
            for rr in range(len(matrix)):
                if matrix[rr][c] == 0:
                    continue
                matrix[rr][c] = '0'
            for cc in range(len(matrix[0])):
                if matrix[r][cc] == 0:
                    continue
                matrix[r][cc] = '0'
                
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    update(r,c)
            
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '0':
                    matrix[r][c] = 0
        
        