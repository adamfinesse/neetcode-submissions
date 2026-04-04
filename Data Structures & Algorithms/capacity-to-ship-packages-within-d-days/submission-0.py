class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        
        min_c = r
        while l<=r:
            c = (l+r)//2

            total_weight = 0
            temp_days=0
            for i in range(len(weights)):
                if total_weight + weights[i] <= c:
                    total_weight +=weights[i]
                else:
                    temp_days+=1
                    total_weight = weights[i]
            if total_weight > 0:
                temp_days +=1

            if temp_days <=days:
                min_c = c
                r=c-1
            else:
                l=c+1
        return min_c
