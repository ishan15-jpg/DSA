# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def length(head: Optional[ListNode]):
            l = 0
            while head:
                l += 1
                head = head.next
            return l

        n = length(head)
        j = n // 2 if n % 2 else n // 2 - 1

        curr,temp,i = head,None,0
        while curr:
            if i == j: 
                temp = curr.next
                curr.next = None
                break
            i += 1
            curr = curr.next

        s,curr = [],temp
        curr = temp
        while curr: 
            temp = curr.next
            curr.next = None
            s.append(curr)
            curr = temp

        curr = head
        while curr and s:
            temp = curr.next
            curr.next = s[-1]
            s[-1].next = temp
            s.pop()
            curr = temp

        return head