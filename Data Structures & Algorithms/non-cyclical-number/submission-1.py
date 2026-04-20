class Solution:
    def isHappy(self, n: int) -> bool:
        sqr = n

        seen = set()
        while sqr != 1:
            num = sqr
            sqr = 0
            while num:
                sqr += math.pow(num % 10,2)
                num //= 10

            if sqr in seen:
                return False
            seen.add(sqr)
                
        return True