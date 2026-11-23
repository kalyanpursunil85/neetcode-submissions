# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        prev, head_s = None, slow.next
        curr = head_s
        while head_s:
            head_s = head_s.next
            curr.next = prev
            prev = curr
            curr = head_s
        
        slow.next = None
        # prev is the beginning of the second half
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2








        