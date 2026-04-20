class Solution:
    def isHappy(self, n: int) -> bool:
        sqr = n

        seen = set()
        while sqr != 1:
            num = sqr
            sum_sqr = 0
            while num:
                sum_sqr += math.pow(num % 10,2)
                num //= 10

            if sum_sqr in seen:
                return False
            seen.add(sum_sqr)
            sqr = sum_sqr
                
        return True