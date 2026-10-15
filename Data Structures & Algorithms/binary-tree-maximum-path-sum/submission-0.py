# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.best = float('-inf')   # najlepszy wynik; start: minus nieskończoność,
                                    # bo wszystkie wartości mogą być ujemne

        def gain(node):
            if not node:
                return 0

            # odnogi ujemne ignorujemy (bierzemy max z 0)
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)

            # ścieżka z tym węzłem jako szczytem łuku
            self.best = max(self.best, node.val + left + right)

            # rodzicowi oddajemy tylko jedną odnogę
            return node.val + max(left, right)

        gain(root)
        return self.best