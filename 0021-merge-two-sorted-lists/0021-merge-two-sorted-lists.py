# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1 or not l2: return l1 if l1 else l2
        dummy = temp = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next
        if l1: temp.next = l1
        if l2: temp.next = l2
        return dummy.next