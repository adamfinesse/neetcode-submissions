class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        stock = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < stock:
                stock = prices[i]
            elif prices[i] > stock:
                total += (prices[i] - stock)
                stock = prices[i]
        return total