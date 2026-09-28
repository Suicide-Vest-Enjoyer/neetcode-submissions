# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        res = []
        que = deque()
        if root:
            res.append((root.val, level))
            que.append((root, level))
        while que:
            dummy, level = que.popleft()
            lvl = 1 + level
            if dummy.left:
                que.append((dummy.left, lvl))
                res.append((dummy.left.val, lvl))
            if dummy.right:
                que.append((dummy.right, lvl))
                res.append((dummy.right.val, lvl))
            
        x = []
        temp = []
        last = 0
        for i in res:
            if i[1] == last:
                temp.append(i[0])
            else:
                x.append(temp)
                temp = [i[0]]
                last += 1
        if temp:
            x.append(temp)
        return x