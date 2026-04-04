class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        def backtrack(arr,seen,i):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            if i == len(nums):
                return

            j=0
            while j < len(nums):
                if (nums[j],j) in seen:
                    j+=1
                    continue
                arr.append(nums[j])
                seen.add((nums[j],j))
                backtrack(arr,seen,i+1)
                arr.pop()
                seen.remove((nums[j],j))
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            
        backtrack([],set(),0)
        return res
            

           
            