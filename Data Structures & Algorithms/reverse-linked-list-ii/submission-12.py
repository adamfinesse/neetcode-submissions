# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node):
            d = ListNode()

            nxt = None
            end = None
            while node:
                d.next = ListNode(node.val,nxt)
                nxt = d.next
                if not end:
                    end = d.next
                node = node.next
            
            return [d.next,end]

        pre,post = None,None
        i = 1
        h = head
        while h:
            if i < left:
                pre = h
                h = h.next
                i+=1
            elif i == left:
                while i < right:
                    h = h.next
                    i+=1
                post = h.next
                h.next = None
                start,end = reverse(pre.next if pre else head)
                if pre:
                    pre.next = start
                else:
                    head = start
                end.next = post
        
                return head
        return head

