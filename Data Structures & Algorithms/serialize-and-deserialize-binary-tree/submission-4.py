class Codec:
    def serialize(self, root):
        out = []
        def walk(node):
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            walk(node.left)
            walk(node.right)
        walk(root)
        return ",".join(out)

    def deserialize(self, data):
        tokens = iter(data.split(","))
        def build():
            tok = next(tokens)
            if tok == "#":
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node
        return build()