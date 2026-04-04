class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        if len(s) <3:
            return True
        def checkValid(sub):
            l,r=0,len(sub)-1
            while l <r:
                if sub[l] != sub[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True

        c=0
        while l <r:
            if s[l] != s[r]:
                return checkValid(s[0:l]+s[l+1:]) or checkValid(s[0:r] + s[r+1:])
            else:
                l+=1
                r-=1
        return True