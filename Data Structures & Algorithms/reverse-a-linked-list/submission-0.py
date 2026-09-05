# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        node = None
        while head != None:
            node = ListNode(head.val, last)
            last = node
            head = head.next
        
        return node






