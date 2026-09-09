# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        while True:
            if head is None or head.next == None:
                return False
            elif head in hashmap.keys():
                return True
            hashmap[head] = ""
            head = head.next
            