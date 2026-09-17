# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque()
        if q is not None and p is not None:
            que.append((p, q))
        elif q is not None or p is not None:
            return False
        elif p is None and q is None:
            return True
        while que:
            p, q = que.popleft()
            if q.val != p.val:
                return False
            if q.left or p.left:
                if q.left and p.left:
                    if q.left.val != p.left.val:
                        return False
                    que.append((q.left, p.left))
                else:
                    return False
            if q.right or p.right:
                if q.right and p.right:
                    if q.right.val != p.right.val:
                        return False
                    que.append((q.right, p.right))
                else:
                    return False
        return True
            
        