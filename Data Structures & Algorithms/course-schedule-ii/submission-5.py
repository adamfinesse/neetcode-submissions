from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        p = prerequisites
        course_map = defaultdict(list)
        indegrees = defaultdict(int)
        for i in range(len(p)):
            course_map[p[i][1]].append(p[i][0])
            indegrees[p[i][0]] +=1
        
        q = deque()
        for i in range(numCourses):
            if not indegrees[i]:
                q.append(i)
        
        res = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                for j in course_map[node]:
                    indegrees[j]-=1
                    if indegrees[j] == 0:
                        q.append(j)
                res.append(node)
            
        return res if len(res) == numCourses else []
