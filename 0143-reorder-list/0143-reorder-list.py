# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find mid node
        slow,fast = head,head.next
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next

        # Reverse second half of LL
        second = slow.next
        prev = slow.next = None 
        while second: 
            temp = second.next
            second.next = prev
            prev,second = second,temp

        # Merge both lists
        second = prev
        while second:
            temp,temp2 = head.next,second.next
            head.next,second.next = second,temp
            head,second = temp,temp2
        # if head : head.next = None