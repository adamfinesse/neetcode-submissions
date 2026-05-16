class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = defaultdict(int)
        min_coins[0] = 0

        for i in range(1,amount+1):
            min_coins[i] = float('inf')
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)
        return min_coins[amount] if min_coins[amount] != float('inf') else -1

                