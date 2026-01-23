#1261. Find Elements in a Contaminated Binary Tree
#Medium
#
#Given a binary tree with the following rules:
#    root.val == 0
#    If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
#    If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
#
#Now the binary tree is contaminated, which means all treeNode.val have been
#changed to -1.
#
#Implement the FindElements class:
#    FindElements(TreeNode* root) Initializes the object with a contaminated
#    binary tree and recovers it.
#    bool find(int target) Returns true if the target value exists in the
#    recovered binary tree.
#
#Example 1:
#Input
#["FindElements","find","find"]
#[[[-1,null,-1]],[1],[2]]
#Output
#[null,false,true]
#Explanation
#FindElements findElements = new FindElements([-1,null,-1]);
#findElements.find(1); // return False
#findElements.find(2); // return True
#
#Constraints:
#    TreeNode.val == -1
#    The height of the binary tree is less than or equal to 20
#    The total number of nodes is between [1, 10^4]
#    Total calls of find() is between [1, 10^4]
#    0 <= target <= 10^6

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    """
    Recover the tree by DFS and store all values in a set.
    """
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self._recover(root, 0)

    def _recover(self, node: Optional[TreeNode], val: int):
        if not node:
            return

        node.val = val
        self.values.add(val)

        self._recover(node.left, 2 * val + 1)
        self._recover(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values


class FindElementsO1:
    """
    Alternative: Don't store values, compute path on the fly.
    """
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        # Trace path from root using target's binary representation
        # target = 0 -> root
        # For target > 0:
        # Path encoded in binary of (target + 1), ignore first bit
        # 0 = left, 1 = right

        target += 1  # Now bit pattern encodes path

        # Find path (read bits from high to low, skip leading 1)
        path = []
        while target > 1:
            path.append(target % 2)
            target //= 2
        path.reverse()

        # Follow path in tree
        node = self.root
        for bit in path:
            if not node:
                return False
            if bit == 0:
                node = node.left
            else:
                node = node.right

        return node is not None
