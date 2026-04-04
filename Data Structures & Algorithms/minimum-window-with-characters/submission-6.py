class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(int)
        equal_count = 0
        total_t_count = len(t_count)
    
        sub = None
        l,r=0,0
        while r <len(s):  
            if s[r] in t_count.keys():
                s_count[s[r]] +=1
                if s_count[s[r]] == t_count[s[r]]:
                    equal_count+=1
                r+=1
            while equal_count == total_t_count:
                if s[l] not in t_count.keys():
                    l+=1
                elif s_count[s[l]]-1 >= t_count[s[l]]:
                    s_count[s[l]]-=1
                    l+=1  
                else:
                    if sub == None or r-l < len(sub):
                        sub = s[l:r]
                    s_count[s[l]]-=1
                    l+=1  
                    equal_count-=1
                    
            
            while l < len(s) and s[l] not in t_count.keys():
                l+=1
            while r < len(s) and s[r] not in t_count.keys():
                r+=1
        return sub if sub != None else ""
            
            
            