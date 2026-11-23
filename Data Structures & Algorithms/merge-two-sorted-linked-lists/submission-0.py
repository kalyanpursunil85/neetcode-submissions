# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        
        dummy = next_node = ListNode()
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val

            if v1 < v2:
                next_node.next = ListNode(v1)
                list1 = list1.next
            else:
                next_node.next = ListNode(v2)
                list2 = list2.next
            
            next_node = next_node.next

        if list1:
            next_node.next = list1
        
        if list2:
            next_node.next = list2
        
        return dummy.next