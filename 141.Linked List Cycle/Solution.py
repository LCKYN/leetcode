# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, h: ListNode) -> bool:
        while h:
            if(h.val == None):
                return True
            h.val = None
            h = h.next
            
        return False