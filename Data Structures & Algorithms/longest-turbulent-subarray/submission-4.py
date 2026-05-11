class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        max_turb = 1
        symbol_arr = []
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                symbol_arr.append(">")
                max_turb = 2
            elif arr[i] < arr[i+1]:
                symbol_arr.append("<")
                max_turb = 2
            else:
                symbol_arr.append("=")

        turb = None
        for i in range(len(symbol_arr)-1):
            if symbol_arr[i] == "=" or symbol_arr[i+1] == "=" or (symbol_arr[i] == symbol_arr[i+1]):
                turb = None
                continue
            if symbol_arr[i] != symbol_arr[i+1]:
                if turb == None:
                    turb=3
                else:
                    turb+=1
                max_turb = max(max_turb,turb)

        return max_turb