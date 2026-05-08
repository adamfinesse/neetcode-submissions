class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete_count = 0

        row = 1
        while True:
            if n-row < 0:
                return complete_count
            complete_count+=1
            n -= row
            row+=1