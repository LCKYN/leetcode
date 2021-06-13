# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode((l1.val + l2.val) % 10)
        temp = res

        c = 0
        if((l1.val + l2.val) >= 10):
            c = 1

        l1 = l1.next
        l2 = l2.next

        while(l1 or l2 or c):
            temp.next = ListNode()
            temp = temp.next

            if(l1 and l2):
                temp.val = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
                c = 0
                if(temp.val >= 10):
                    temp.val %= 10
                    c += 1
            elif(l1):
                temp.val = l1.val + c
                l1 = l1.next
                c = 0
                if(temp.val >= 10):
                    temp.val %= 10
                    c += 1
            elif(l2):
                temp.val = l2.val + c
                l2 = l2.next
                c = 0
                if(temp.val >= 10):
                    temp.val %= 10
                    c += 1
            elif(c):
                temp.val = 1
                c = 0
            else:
                break

        return res
