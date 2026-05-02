class Solution:
    def maxDifference(self, s: str) -> int:
        alpha_freq = [0]*26
        
        for c in s:
            alpha_freq[ord(c)-ord('a')] +=1
        
        min_even,max_even,min_odd,max_odd = float('inf'), float('-inf'), float('inf'), float('-inf')

        for i in range(len(alpha_freq)):
            num = alpha_freq[i]
            if num % 2 == 1:
                min_odd = min(min_odd,num)
                max_odd = max(max_odd,num)
            elif num != 0 and num %2 == 0:
                min_even = min(min_even,num)
                max_even = max(max_even,num)

        return max(max_odd - min_even, min_odd - max_even)