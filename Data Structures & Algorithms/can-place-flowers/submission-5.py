class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placable = 0
        i=0
        while i <len(flowerbed)-1:
            if flowerbed[i] == 0 and flowerbed[i+1] == 1:
                i+=3
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                placable +=1
                i+=2
            else:
                i+=2

        if i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            placable+=1
        return placable >= n
            
        