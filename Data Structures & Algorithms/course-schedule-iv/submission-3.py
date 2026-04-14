class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_map = defaultdict(list)

        for p in prerequisites:
            course_map[p[0]].append(p[1])

        prereq_map = defaultdict(bool)
        visited = set()
        def dfs(i,j):
            if (i,j) in visited:
                return
            prereq_map[(i,j)] = True
            visited.add((i,j))
            for k in course_map[j]:
                prereq_map[(i,k)] = True
                dfs(i,k)
            return 
            
        for i in range(numCourses):
            dfs(i,i)

        res = []
        for q in queries:
            f,s = q
            res.append(prereq_map[(f,s)])
        return res