# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1, head)
        curr = dummy
        while curr.next and curr.next.next:
            a, b = curr.next, curr.next.next
            a.next = b.next
            b.next = a
            curr.next = b
            curr = a
                
        return dummy.next
        
