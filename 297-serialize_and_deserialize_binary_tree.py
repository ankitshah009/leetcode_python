#297. Serialize and Deserialize Binary Tree
#Hard
#
#Serialization is the process of converting a data structure or object into a sequence of bits
#so that it can be stored in a file or memory buffer, or transmitted across a network connection
#link to be reconstructed later in the same or another computer environment.
#
#Design an algorithm to serialize and deserialize a binary tree.
#
#Example 1:
#Input: root = [1,2,3,null,null,4,5]
#Output: [1,2,3,null,null,4,5]
#
#Example 2:
#Input: root = []
#Output: []
#
#Constraints:
#    The number of nodes in the tree is in the range [0, 10^4].
#    -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "null"

        result = []

        def preorder(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = iter(data.split(","))

        def build():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
