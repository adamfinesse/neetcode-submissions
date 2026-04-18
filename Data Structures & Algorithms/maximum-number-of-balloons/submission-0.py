class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_count = Counter(text)

        cnt = 0
        while True:
            for c in "balloon":
                if letter_count[c]:
                    letter_count[c]-=1
                else:
                    return cnt
            cnt+=1