class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append([position[i],speed[i]])
        stack.sort()
        
        res=0
        i = len(stack)-1
        while i >0:
            ToA_1 = (target-stack[i][0])/stack[i][1]
            ToA_2 = (target-stack[i-1][0])/stack[i-1][1]
            if ToA_1 >= ToA_2:
                stack.pop(i-1)
            i-=1
           
        return len(stack)
            

