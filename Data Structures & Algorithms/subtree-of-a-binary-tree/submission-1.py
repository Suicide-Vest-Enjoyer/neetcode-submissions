# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        que = deque([root])
        mabe = deque()
        while que:
            dummy = que.pop()
            if dummy.left:
                que.append(dummy.left)
            if dummy.right:
                que.append(dummy.right)
            if subRoot.val == dummy.val:
                mabe.append((dummy, subRoot))

        print(mabe)
        while mabe:
            l, r = mabe.popleft()
            sub = deque()
            sub.append((l, r))
            while sub:
                p, q = sub.popleft()
                if p.val != q.val:
                    break
                if p.left is None and q.left is not None:
                    break
                if p.left is not None and q.left is None:
                    break
                if p.right is None and q.right is not None:
                    break
                if p.right is not None and q.right is None:
                    break
                if p.left and q.left:
                    sub.append((p.left, q.left))
                if p.right and q.right:
                    sub.append((p.right, q.right))
                if len(sub) == 0:
                    return True
            
        return False