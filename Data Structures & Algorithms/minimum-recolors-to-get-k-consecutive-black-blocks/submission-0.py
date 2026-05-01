class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,r=0,0

        min_ops = float('inf')
        w_cnt = 0
        while r < len(blocks):
            if r-l < k:
                if blocks[r] == "W":
                    w_cnt+=1
                r+=1
            if r-l == k:
                min_ops = min(min_ops,w_cnt)
                if blocks[l] == "W":
                    w_cnt -=1
                l+=1 

        return min_ops

      

        
