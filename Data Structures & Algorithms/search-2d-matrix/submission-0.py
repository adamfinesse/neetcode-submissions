class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l_mat,r_mat = 0,len(matrix)-1

        while l_mat<=r_mat:
            m_mat = (l_mat+r_mat) //2

            if matrix[m_mat][0] <= target and matrix[m_mat][-1] >= target:
                l,r=0,len(matrix[m_mat])-1

                while l<=r:
                    m=(l+r)//2
                    if matrix[m_mat][m] == target:
                        return True
                    if matrix[m_mat][m] < target:
                        l=m+1
                    else:
                        r=m-1
                return False
            elif matrix[m_mat][-1] < target:
                l_mat = m_mat+1
            else:
                r_mat = m_mat-1
        return False