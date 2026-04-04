class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        def backtrack(arr,seen):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            j=0
            while j < len(nums):
                if j in seen:
                    j+=1
                    continue
                arr.append(nums[j])
                seen.add(j)
                backtrack(arr,seen)
                arr.pop()
                seen.remove(j)
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            
        backtrack([],set())
        return res
            

           
            