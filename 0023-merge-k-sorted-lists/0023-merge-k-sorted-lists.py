# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def divide(self, lists: list[ListNode | None], l: int, r: int) -> ListNode | None:
        if l > r: return None
        if l == r: return lists[l]
        mid = (l+r) >> 1
        left = self.divide(lists,l,mid)
        right = self.divide(lists,mid+1,r)
        return self.conquer(left,right)

    def conquer(self, left: ListNode | None, right: ListNode | None) -> ListNode | None:
        if not left or not right: return left if left else right
        dummy = res = ListNode(-1)
        while left and right:
            if left.val < right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        if left: res.next = left
        if right: res.next = right
        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists: return None
        return self.divide(lists,0,len(lists)-1)