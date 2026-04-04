class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in rows[i] or num in cols[j] or num in sub_box[(i//3,j//3)]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                sub_box[(i//3,j//3)].add(num)
        return True


