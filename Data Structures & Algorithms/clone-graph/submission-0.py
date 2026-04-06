"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = set()
        clone_map = {}

        def dfs(n):
            if not n or n in seen:
                return
            seen.add(n)
            if n not in clone_map:
                clone_map[n] = Node(n.val)

            for neighbor in n.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                clone_map[n].neighbors.append(clone_map[neighbor])
                dfs(neighbor)
        dfs(node)
        return clone_map[node] if node else None
                