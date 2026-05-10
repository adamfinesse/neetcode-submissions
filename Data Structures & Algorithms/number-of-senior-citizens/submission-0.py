class Solution:
    def countSeniors(self, details: List[str]) -> int:
       cnt = 0
       for s in details:
        if int(s[-4:-2]) > 60:
            cnt+=1
       return cnt
