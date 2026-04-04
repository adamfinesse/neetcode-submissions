class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0,0

        while r <len(arr):
            if r-l+1 <= k:
                r+=1
            elif abs(arr[r]-x) < abs(arr[l]-x) or (abs(arr[l]-x) == abs(arr[r]-x) and arr[r] < arr[l]):
                l+=1
            elif r-l+1 >= k and arr[r] == arr[l]:
                l+=1
            else:
                return arr[l:r]
        return arr[l:r]
            