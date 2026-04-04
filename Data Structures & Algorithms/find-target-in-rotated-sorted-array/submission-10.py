class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot, to know which array to search (left or right half)
        l,r = 0,len(nums)-1
        pivot = 0
        while l<r:
            m = (l+r)//2

            if m > 0 and nums[m] < nums[m-1]:
                pivot = m
                break
            if nums[m] > nums[r]:
                l=m+1
            else:
                r =m-1
        if l == r:
            pivot = l
        print(pivot)
        if pivot != 0 and nums[0] <= target and nums[pivot-1] >= target:
            l=0
            r = pivot
        else:
            l=pivot
            r=len(nums)-1
        print(l,r)
        while l<=r:
            m = (l+r) //2

            if nums[m] == target:
                return m
            if nums[m] < target:
                l=m+1
            else:
                r=m-1
        return -1
