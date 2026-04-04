class StockSpanner:

    def __init__(self):
        self.daily_prices = []

    def next(self, price: int) -> int:
        span = 1
        i = len(self.daily_prices)-1
        while i >= 0 and self.daily_prices[i][0] <= price:
            span+=self.daily_prices.pop()[1]
            i-=1
        self.daily_prices.append([price,span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)