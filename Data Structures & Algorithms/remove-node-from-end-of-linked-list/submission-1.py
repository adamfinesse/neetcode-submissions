# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        h = head
        while h:
            list_len+=1
            h = h.next
        
        p = None
        cur = head
        cnt = 0
        while cur and cnt != (list_len - n):
            p = cur
            cur = cur.next
            cnt +=1
        if p:
            p.next = cur.next
        else:
            head = head.next
        return head