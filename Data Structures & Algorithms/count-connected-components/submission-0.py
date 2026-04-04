class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        visited = set()
        count = 0
        for node,con_node in edges:
            adjList[node].append(con_node) 
            adjList[con_node].append(node)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for edge in adjList[node]:
                dfs(edge)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count
            
