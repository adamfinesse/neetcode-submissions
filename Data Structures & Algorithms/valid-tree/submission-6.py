class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for node,edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        
        visited = set()
        
        def dfs(p,e):
            if e in visited:
                return False
            
            visited.add(e)
            for edge in adj[e]:
                if edge == p:
                    continue
                if not dfs(e,edge):
                    return False
            return True
        
        return dfs(-1,0) and len(visited) == n