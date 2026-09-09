# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while True:
            if head is None or head.next == None:
                return False
            elif head in visited:
                return True
            visited.add(head)
            head = head.next
            