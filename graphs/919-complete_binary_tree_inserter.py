#919. Complete Binary Tree Inserter
#Medium
#
#A complete binary tree is a binary tree in which every level, except possibly
#the last, is completely filled, and all nodes in the last level are as far left
#as possible.
#
#Design an algorithm to insert a new node to a complete binary tree keeping it
#complete after the insertion.
#
#Implement the CBTInserter class:
#- CBTInserter(TreeNode root) Initializes the data structure with the root.
#- int insert(int val) Inserts a new node with val to the tree, returns the
#  value of the parent of the inserted node.
#- TreeNode get_root() Returns the root node of the tree.
#
#Example 1:
#Input: ["CBTInserter","insert","insert","get_root"]
#       [[[1,2]],[3],[4],[]]
#Output: [null,1,2,[1,2,3,4]]
#
#Constraints:
#    The number of nodes in the tree will be in the range [1, 1000].
#    0 <= Node.val <= 5000
#    root is a complete binary tree.
#    At most 10^4 calls will be made to insert and get_root.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    """
    BFS to find nodes that can accept children.
    """

    def __init__(self, root: TreeNode):
        self.root = root
        self.deque = deque()

        # BFS to find nodes that can accept children
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.deque[0]

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.deque.popleft()

        self.deque.append(new_node)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


class CBTInserterList:
    """Store all nodes in list, use index math"""

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = []

        # Level order to build list
        queue = deque([root])
        while queue:
            node = queue.popleft()
            self.nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        n = len(self.nodes)
        parent_idx = (n - 1) // 2
        parent = self.nodes[parent_idx]

        if n % 2 == 1:  # Left child
            parent.left = new_node
        else:  # Right child
            parent.right = new_node

        self.nodes.append(new_node)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root
