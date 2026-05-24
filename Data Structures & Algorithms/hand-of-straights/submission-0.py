class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        total_cards =len(hand)
        if total_cards % groupSize != 0:
            return False

        cnt = Counter(hand)
        
        while total_cards >0:
            key = min(cnt.keys())
            for i in range(groupSize):
                if cnt.get(key,0) == 0:
                    return False
                cnt[key] -=1
                total_cards -=1
                if cnt[key] == 0:
                    del cnt[key]            
                key +=1

        return True