class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=prices[0]
        p =0
        for i in range(1,len(prices)):
            if prices[i] < l:
                l = prices[i]
            elif prices[i]-l > p:
                p = (prices[i]-l)
        return p