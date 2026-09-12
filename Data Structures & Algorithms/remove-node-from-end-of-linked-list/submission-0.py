# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        hashmap = {}
        i = 0
        while node:
            hashmap[i] = node
            node = node.next
            i += 1
        index = max(hashmap.keys()) + 1 - n
        if index == 0:
            head = head.next
        else:
            hashmap[index-1].next = hashmap[index].next
        return head