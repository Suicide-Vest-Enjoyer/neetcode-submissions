import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        counter = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode()
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next