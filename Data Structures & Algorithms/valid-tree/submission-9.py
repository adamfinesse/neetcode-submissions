class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        for e in edges:
            adj_map[e[0]].append(e[1])
            adj_map[e[1]].append(e[0])
        print(adj_map)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in range(len(adj_map[i])):
                if prev == adj_map[i][j]:
                    continue
                if not dfs(adj_map[i][j],i):
                    return False
            return True
        
        if not dfs(0,None):
            return False
        
        return len(visited)== n
        
            