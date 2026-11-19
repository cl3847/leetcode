# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def traverse(head, queue):
            if not head:
                return True
            
            queue.append(head.val)
            nxt = traverse(head.next, queue)

            opp = queue.popleft()
            return nxt and opp == head.val
        
        return traverse(head, deque())
