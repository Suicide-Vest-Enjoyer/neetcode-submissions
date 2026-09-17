# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        best = 1
        que = []
        cur = root
        dep = 1
        while que or cur.left or cur.right:
            if cur.right:
                que.append((cur.right, dep+1))
            if cur.left != None:
                cur = cur.left
                dep += 1
            else:
                cur,dep = que.pop()
            best = max(best, dep)
        return best