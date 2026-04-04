
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclideanDist(x1,x2,y1,y2):
            return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
        points = [(euclideanDist(p[0], 0, p[1], 0), p) for p in points]
        heapq.heapify(points)

        #print(points)
        res = []
        while k:
            dist_point = heapq.heappop(points)
            res.append(dist_point[1])
            k-=1
        return res