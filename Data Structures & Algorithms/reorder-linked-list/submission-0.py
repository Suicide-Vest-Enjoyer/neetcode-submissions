class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hashmap = {}
        node = head
        i = 0

        while node:
            hashmap[i] = node
            node = node.next
            i += 1

        left = 0
        right = i - 1
        node = head

        while left < right:
            left_node = hashmap[left]
            right_node = hashmap[right]

            next_node = left_node.next

            left_node.next = right_node
            right_node.next = next_node

            node = next_node
            left += 1
            right -= 1

        node.next = None
