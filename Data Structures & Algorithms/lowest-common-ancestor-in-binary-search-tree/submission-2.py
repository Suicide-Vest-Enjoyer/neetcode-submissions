# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        que = deque([(root, [root])])
        res = []
        while que:
            dummy, ans = que.popleft()
            if dummy.left:
                pas1 = ans + [dummy.left] 
                que.append((dummy.left, pas1))
            if dummy.right:
                pas2 = ans + [dummy.right] 
                que.append((dummy.right, pas2))
            if dummy.val == p.val or dummy.val == q.val:
                res.append(ans)
                if len(res) > 1:
                    break

        p = res[0]
        p.reverse()
        q = res[1]
        for i in p:
            if i in q:
                return i
        

        