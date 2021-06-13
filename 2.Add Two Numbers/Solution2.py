# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        eq1 = 0
        eq2 = 0
        
        temp = 1
        
        while(l1 != None):
            eq1 = l1.val * temp + eq1
            l1 = l1.next
            temp *= 10
            
        temp = 1
        
        while(l2 != None):
            eq2 = l2.val * temp + eq2
            l2 = l2.next
            temp *= 10
            
        return map(int,str(eq1+eq2))[::-1]