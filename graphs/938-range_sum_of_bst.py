#938. Range Sum of BST
#Easy
#
#Given the root node of a binary search tree and two integers low and high,
#return the sum of values of all nodes with a value in the inclusive range
#[low, high].
#
#Example 1:
#Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32
#Explanation: Nodes 7, 10, 15 are in the range [7, 15]. 7+10+15 = 32.
#
#Example 2:
#Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
#Output: 23
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 2 * 10^4].
#    1 <= Node.val <= 10^5
#    1 <= low <= high <= 10^5
#    All Node.val are unique.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        DFS with pruning using BST property.
        """
        if not root:
            return 0

        if root.val < low:
            # All values in left subtree are also < low
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            # All values in right subtree are also > high
            return self.rangeSumBST(root.left, low, high)

        # root.val is in range
        return (root.val +
                self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high))


class SolutionIterative:
    """Iterative BFS"""

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue

            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
            if low <= node.val <= high:
                total += node.val

        return total


class SolutionInorder:
    """In-order traversal with early termination"""

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if node.val > high:
                break

            if node.val >= low:
                total += node.val

            node = node.right

        return total
