# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        c = head
        while c:
            # print("c", c)
            if(c.next and c.next.val == val):
                c.next = c.next.next
            else:
                c = c.next
        # print("h", head)
        return head.next if head and head.val == val else head