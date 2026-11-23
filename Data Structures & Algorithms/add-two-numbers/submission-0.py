# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: return
        
        if l1 and not l2:
            return l1
        
        if not l1 and l2:
            return l2
        
        carry = 0
        dummy = next_node = ListNode()

        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            carry, v = divmod(v1+v2+carry, 10)
            next_node.next = ListNode(v)
            next_node = next_node.next
        
        return dummy.next
            
