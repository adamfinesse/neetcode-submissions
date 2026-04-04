class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(i,r,c,seen):
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r,c) in seen:
                return False
            if len(word)-1 == i and word[i] == board[r][c]:
                return True
            if board[r][c] == word[i]:
                seen.add((r,c))
                if (
                backtrack(i+1,r+1,c,seen) or
                backtrack(i+1,r-1,c,seen) or
                backtrack(i+1,r,c+1,seen) or
                backtrack(i+1,r,c-1,seen)
                ):
                    return True
                seen.remove((r,c))
            
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(0,r,c,set()):
                        return True
        return False

        