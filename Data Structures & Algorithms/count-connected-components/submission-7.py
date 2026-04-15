class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)

            for j in adj_list[i]:
                dfs(j)

        cnt = 0
        for k in range(n):
            if k not in visited:
                dfs(k)
                cnt+=1
        return cnt

