class Codec:
    # format: "<val>(<len_left>)<left><right>"

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"{root.val}({len(left)}){left}{right}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        open_i = data.index("(")
        close_i = data.index(")", open_i)
        left_len = int(data[open_i + 1:close_i])
        left_start = close_i + 1
        left_end = left_start + left_len

        root = TreeNode(int(data[:open_i]))
        root.left = self.deserialize(data[left_start:left_end])
        root.right = self.deserialize(data[left_end:])
        return root