# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()

        cur = h
        carry = 0
        while l1 or l2:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = 0

            if total >= 10:
                carry = 1
                total = total % 10

            cur.next = ListNode(total)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            cur.next = ListNode(1)

        return h.next
            