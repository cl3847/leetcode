# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(-inf, head)
        head = dummy

        front = None
        for _ in range(left):
            front = head
            head = head.next
        
        back = None
        prev = None
        for _ in range (right - left + 1):
            if back is None:
                back = head
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        if back:
            back.next = head
        front.next = prev

        return dummy.next
        
        




            

            
            

                
        
            
