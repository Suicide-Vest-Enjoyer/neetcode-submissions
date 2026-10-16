# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root or root is None:
            return ""
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        s = int(2 + len(l))
        if len(str(s + len(str(s)))) > len(str(s)):
            s = len(str(s + len(str(s))))
        else:
            s += len(str(s))
        return f"{root.val}(_{s}_{l})[{r}]"
   
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #print("------------------------------------------")
        #print(f"Data: {data}")
        if data == "":
            return 
        r = ""
        for i in range(len(data)):
            if data[i] == "(" or data[i] == "[":
                break
            r += data[i]
        #print(f"R1: {r}")
        root = TreeNode(int(r))
        data = data[len(r)+2:]
        r = ""
        for i in range(len(data)):
            if data[i] == "_":
                break
            r += data[i]
        #print(f"R2: {r}")
        #print(f"Data: {data}")
        l = data[1+len(r):int(r)-1]
        r = data[int(r)+1:len(data)-1]
        #print(f"L: {l}")
        #print(f"R: {r}")
        root.left = self.deserialize(l)
        root.right = self.deserialize(r)
        return root


