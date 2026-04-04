class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(w,r,c,seen):
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r,c) in seen:
                return False
            if w[0] == board[r][c] and len(w) == 1:
                return True
            if board[r][c] == w[0]:
                seen.add((r,c))
                if (
                backtrack(w[1:],r+1,c,seen) or
                backtrack(w[1:],r-1,c,seen) or
                backtrack(w[1:],r,c+1,seen) or
                backtrack(w[1:],r,c-1,seen)
                ):
                    return True
                seen.remove((r,c))
            
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(word,r,c,set()):
                        print("found")
                        return True
        return False

        