#1586. Binary Search Tree Iterator II
#Medium
#
#Implement the BSTIterator class that represents an iterator over the in-order
#traversal of a binary search tree (BST):
#
#- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
#  The root of the BST is given as part of the constructor. The pointer should
#  be initialized to a non-existent number smaller than any element in the BST.
#- boolean hasNext() Returns true if there exists a number in the traversal to
#  the right of the pointer, otherwise returns false.
#- int next() Moves the pointer to the right, then returns the number at the pointer.
#- boolean hasPrev() Returns true if there exists a number in the traversal to
#  the left of the pointer, otherwise returns false.
#- int prev() Moves the pointer to the left, then returns the number at the pointer.
#
#Notice that by initializing the pointer to a non-existent smallest number,
#the first call to next() will return the smallest element in the BST.
#
#You may assume that next() and prev() calls will always be valid. That is,
#there will be at least a next/previous number in the in-order traversal when
#next()/prev() is called.
#
#Example 1:
#Input: ["BSTIterator", "next", "next", "prev", "next", "hasNext", "next", "next", "next", "hasNext", "hasPrev", "prev", "prev"]
#       [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], [], [], [], []]
#Output: [null, 3, 7, 3, 7, true, 9, 15, 20, false, true, 15, 9]
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^5].
#    0 <= Node.val <= 10^6
#    At most 10^5 calls will be made to hasNext, next, hasPrev, and prev.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Store visited nodes in a list for O(1) prev/next after first visit.
    Use lazy evaluation - only traverse when needed.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.arr = []  # Stores visited nodes
        self.pointer = -1  # Current position (-1 means before first)

        # Initialize stack for in-order traversal
        self._push_left(root)

    def _push_left(self, node: TreeNode) -> None:
        """Push all left children onto stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr) - 1 or self.stack

    def next(self) -> int:
        self.pointer += 1

        # If we've already visited this position
        if self.pointer < len(self.arr):
            return self.arr[self.pointer]

        # Need to get next from BST
        node = self.stack.pop()
        self._push_left(node.right)
        self.arr.append(node.val)

        return node.val

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]


class BSTIteratorFullTraversal:
    """
    Alternative: Do full in-order traversal upfront.
    Simpler but uses O(n) space from start.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.pointer = -1
        self._inorder(root)

    def _inorder(self, node: TreeNode) -> None:
        if not node:
            return
        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr) - 1

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]


class BSTIteratorGenerator:
    """
    Using generator for lazy evaluation.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.pointer = -1
        self.gen = self._inorder_gen(root)

    def _inorder_gen(self, node: TreeNode):
        if not node:
            return
        yield from self._inorder_gen(node.left)
        yield node.val
        yield from self._inorder_gen(node.right)

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr) - 1 or self._advance_gen()

    def _advance_gen(self) -> bool:
        """Try to get next value from generator."""
        try:
            val = next(self.gen)
            self.arr.append(val)
            return True
        except StopIteration:
            return False

    def next(self) -> int:
        self.pointer += 1
        if self.pointer >= len(self.arr):
            self._advance_gen()
        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]
