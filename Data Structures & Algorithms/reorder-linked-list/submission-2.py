# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return
        s,f = head,head
        # get mid point of list
        p = None
        while f and f.next:
            p = s
            s = s.next
            f = f.next.next
        p.next = None
  
        #reverse second half
        l2 = ListNode()
        cur = None
        while s:
            l2.next = s
            s = s.next
            l2.next.next = cur
            cur = l2.next
        l2 = l2.next

        # combine them while both have values
        l1 = head
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            t1 = l1.next
            cur.next = l1
            l1=t1
            cur = cur.next

            t2 = l2.next
            cur.next = l2
            l2=t2
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
             


        