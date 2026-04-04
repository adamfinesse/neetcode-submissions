# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = ListNode()
        p=None
        while head:
            next = head.next
            h.next = head
            head.next = p
            p = head

            head = next
        return h.next