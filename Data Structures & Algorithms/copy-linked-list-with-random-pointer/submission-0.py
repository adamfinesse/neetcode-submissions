"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {}

        h = head
        h_d = d = Node(2,None,None)
        while h:
            cur = copy_map.get(h,None)
            if cur:
                d.next = cur
            else:
                copy_map[h] = Node(h.val,None,None)
                d.next = copy_map[h]

            cur_rand = copy_map.get(h.random,None)
            if cur_rand:
                d.next.random = cur_rand
            else:
                copy_map[h.random] = Node(h.random.val,None,None) if h.random else None
                d.next.random = copy_map[h.random]
            d = d.next
            h = h.next

        return h_d.next
            