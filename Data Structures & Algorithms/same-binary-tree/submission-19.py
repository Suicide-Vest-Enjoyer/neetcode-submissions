class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque()
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        que.append((p, q))

        while que:
            p, q = que.popleft()

            if p.val != q.val:
                return False

            if p.left is None and q.left is not None:
                return False
            if p.left is not None and q.left is None:
                return False
            if p.left and q.left:
                que.append((p.left, q.left))

            if p.right is None and q.right is not None:
                return False
            if p.right is not None and q.right is None:
                return False
            if p.right and q.right:
                que.append((p.right, q.right))

        return True