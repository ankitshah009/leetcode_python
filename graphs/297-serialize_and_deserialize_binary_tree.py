#297. Serialize and Deserialize Binary Tree
#Hard
#
#Serialization is the process of converting a data structure or object into a
#sequence of bits so that it can be stored in a file or memory buffer, or
#transmitted across a network connection link.
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

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """Preorder DFS serialization"""

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def preorder(node):
            if not node:
                return ['null']

            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        return ','.join(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = iter(data.split(','))

        def build():
            val = next(values)

            if val == 'null':
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()

            return node

        return build()


class CodecBFS:
    """Level-order (BFS) serialization"""

    def serialize(self, root):
        if not root:
            return ''

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')

        # Remove trailing nulls
        while result and result[-1] == 'null':
            result.pop()

        return ','.join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # Left child
            if i < len(values) and values[i] != 'null':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != 'null':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


class CodecParens:
    """Using parentheses notation"""

    def serialize(self, root):
        if not root:
            return ''

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        if not left and not right:
            return str(root.val)

        return f'{root.val}({left})({right})'

    def deserialize(self, data):
        if not data:
            return None

        # Find first '(' or end of string
        paren_idx = data.find('(')

        if paren_idx == -1:
            return TreeNode(int(data))

        root = TreeNode(int(data[:paren_idx]))

        # Find matching ')' for left subtree
        count = 0
        for i in range(paren_idx, len(data)):
            if data[i] == '(':
                count += 1
            elif data[i] == ')':
                count -= 1
                if count == 0:
                    left_end = i
                    break

        root.left = self.deserialize(data[paren_idx+1:left_end])
        root.right = self.deserialize(data[left_end+2:-1])

        return root
