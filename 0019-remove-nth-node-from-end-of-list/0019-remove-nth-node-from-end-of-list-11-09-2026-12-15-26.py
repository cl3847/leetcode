# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        def walk(head, n):
            if head is None:
                return n
            count = walk(head.next, n) - 1
            if count == 0:
                head.next = head.next.next
            return count

        dummy = ListNode(-1, head)
        walk(dummy, n+1)
        return dummy.next