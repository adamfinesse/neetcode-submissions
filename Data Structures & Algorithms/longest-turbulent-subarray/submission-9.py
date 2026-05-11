class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        max_turb = 1
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                max_turb = 2
                break
            elif arr[i] < arr[i+1]:
                max_turb = 2
                break

        sign = None
        turb = None
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                current = "<"
            elif arr[i] > arr[i+1]:
                current = ">"
            else:
                sign = None
                turb = None
                continue
            
            if current != sign and sign is not None:
                turb += 1
            else:
                turb = 2
            
            sign = current
            max_turb = max(max_turb, turb)

        return max_turb