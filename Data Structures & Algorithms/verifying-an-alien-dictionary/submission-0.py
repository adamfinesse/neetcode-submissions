class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_orders = {}
        for i,c in enumerate(order):
            char_orders[c] = i

        for i in range(len(words)-1):
            for c in range(len(words[i])):
                if len(words[i+1]) <= c: # case where word 2 is same but shorter than word 1
                    return False
                if char_orders[words[i][c]] > char_orders[words[i+1][c]]:
                    return False
                elif char_orders[words[i][c]] == char_orders[words[i+1][c]]:
                    continue
                else:
                    break
        return True
