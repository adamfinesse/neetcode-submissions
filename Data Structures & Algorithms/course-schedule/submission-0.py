from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p = prerequisites
        course_map = defaultdict(list)
        
        for i in range(len(p)):
            course_map[p[i][1]].append(p[i][0])
        
        def dfs(i,visited):
            if i in visited:
                return False
            visited.add(i)
            for c in course_map[i]:
                if not dfs(c,visited):
                    return False
            visited.remove(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
            
        return True
            
            
                
