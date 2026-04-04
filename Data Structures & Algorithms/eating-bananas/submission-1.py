class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)

        min_k = r
        while l<=r:
            k = (l+r)//2
            hrs = 0
            for b in piles:
                hrs += math.ceil(b/k)
            if hrs <= h:
                min_k = k
                r = k-1
            else:
                l = k+1
        return min_k