# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = tail = ListNode(0, None)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = ListNode(list1.val, None)
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val, None)
                tail = tail.next
                list2 = list2.next
        
        tail.next = list1 or list2
        return head.next
