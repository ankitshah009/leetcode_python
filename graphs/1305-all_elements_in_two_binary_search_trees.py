#1305. All Elements in Two Binary Search Trees
#Medium
#
#Given two binary search trees root1 and root2, return a list containing all
#the integers from both trees sorted in ascending order.
#
#Example 1:
#Input: root1 = [2,1,4], root2 = [1,0,3]
#Output: [0,1,1,2,3,4]
#
#Example 2:
#Input: root1 = [1,null,8], root2 = [8,1]
#Output: [1,1,8,8]
#
#Constraints:
#    The number of nodes in each tree is in the range [0, 5000].
#    -10^5 <= Node.val <= 10^5

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Inorder traversal of both trees, then merge two sorted lists.
        """
        def inorder(node, result):
            if not node:
                return
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)

        # Merge two sorted lists
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])

        return result


class SolutionIterator:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """Using iterative inorder with stacks - merge on the fly"""
        def push_left(stack, node):
            while node:
                stack.append(node)
                node = node.left

        stack1, stack2 = [], []
        push_left(stack1, root1)
        push_left(stack2, root2)

        result = []

        while stack1 or stack2:
            # Choose smaller top
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                node = stack1.pop()
                result.append(node.val)
                push_left(stack1, node.right)
            else:
                node = stack2.pop()
                result.append(node.val)
                push_left(stack2, node.right)

        return result


class SolutionGenerator:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """Using generators for inorder traversal"""
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        import heapq
        return list(heapq.merge(inorder(root1), inorder(root2)))
