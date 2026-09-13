# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        checkpoints = []
        if root:
            dummy = root
            checkpoints.append(dummy)

        while checkpoints:
            if dummy.left != None and dummy.right != None:
                checkpoints.append(dummy.right)
                dummy = dummy.left
            elif dummy.left != None:
                dummy = dummy.left
            elif dummy.right != None:
                dummy = dummy.right
            #elif dummy.left == None and dummy.right == None:
            else:
                dummy = checkpoints.pop()
            right = dummy.left
            left = dummy.right
            dummy.left = left
            dummy.right = right

        return root