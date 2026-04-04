class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subsets = [0] * k
        subset_partition = total //k
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(len(subsets)):
                if subsets[j] + nums[i] <= subset_partition:
                    subsets[j]+= nums[i]
                    if backtrack(i+1):
                        return True
                    if nums[i] == subset_partition:
                        break
                    subsets[j] -= nums[i]
            return False
        return backtrack(0)
