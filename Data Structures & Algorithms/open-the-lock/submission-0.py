from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque(["0000"])
        seen = set()
        if "0000" in deadends:
            return -1

        min_turns = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == target:
                    return min_turns
                #positive
                for j in range(4):
                    dial_turned = node[0:j] + str((int(node[j]) + 1)%10) + node[j+1:]
                    if dial_turned in deadends or dial_turned in seen:
                        continue
                    seen.add(dial_turned)
                    q.append(dial_turned)

                for j in range(4):
                    dial_turned = node[0:j] + str((int(node[j]) - 1)%10) + node[j+1:]
                    if dial_turned in deadends or dial_turned in seen:
                        continue
                    seen.add(dial_turned)
                    q.append(dial_turned)
            min_turns +=1
            
        return -1
                
