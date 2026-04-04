class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(substring):
            if len(substring) %2 == 1:
                l,r=len(substring)//2,len(substring)//2
                while l>=0 and r <len(substring):
                    if substring[l] == substring[r]:
                        l-=1
                        r+=1
                    else:
                        return False
            else:
                l,r=(len(substring)//2)-1,len(substring)//2
                while l>=0 and r <len(substring):
                    if substring[l] == substring[r]:
                        l-=1
                        r+=1
                    else:
                        return False
            return True

        def backtrack(arr,j):
            if j == len(s):
                res.append(arr.copy())
                return
            
            for i in range(j,len(s)):
                if isPalindrome(s[j:i+1]):
                    arr.append(s[j:i+1])
                    backtrack(arr,i+1)
                    arr.pop()

        backtrack([],0)
        return res
        