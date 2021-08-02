# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(not l1 and not l2):
            return None
        
        res = ListNode()
        l = res
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                l.val = l1.val
                l1 = l1.next
            else:
                l.val = l2.val
                l2 = l2.next
            l.next = ListNode()
            l = l.next

            
        while(l1 != None):
            l.val = l1.val
            l1 = l1.next
            if(l1):
                l.next = ListNode()
                l = l.next
            
        while(l2 != None):
            l.val = l2.val
            l2 = l2.next
            if(l2):
                l.next = ListNode()
                l = l.next
                
        return res