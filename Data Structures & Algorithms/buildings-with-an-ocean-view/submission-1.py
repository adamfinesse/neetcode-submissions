class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_view = -1
        
        res = []
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_view:
                res.insert(0,i)
                max_view = heights[i]
        
        return res