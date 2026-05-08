class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete_count = 0

        row = 1
        while n >= row:
            n -= row
            if n >=0:
                complete_count +=1
            row+=1
        return complete_count