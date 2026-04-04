class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subsets = [0] * k
        subset_partition = total //k
        nums.sort(reverse=True)

        def backtrack(start,j,seen):
            if j == k or subsets[j] == subset_partition:
                return True
            
            for i in range(start,len(nums)):
                if i not in seen and subsets[j] + nums[i] <= subset_partition:
                    subsets[j] += nums[i]
                    seen.add(i)
                    next_j = j+1 if subsets[j] == subset_partition else j
                    start = 0 if subsets[j] == subset_partition else i
                    if backtrack(start,next_j,seen):
                        return True
                    if nums[i] == subset_partition:
                        break
                    subsets[j] -= nums[i]
                    seen.remove(i)
            return False
            
        return backtrack(0,0,set())
