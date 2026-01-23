#1457. Pseudo-Palindromic Paths in a Binary Tree
#Medium
#
#Given a binary tree where node values are digits from 1 to 9. A path in the
#binary tree is said to be pseudo-palindromic if at least one permutation of
#the node values in the path is a palindrome.
#
#Return the number of pseudo-palindromic paths going from the root node to leaf
#nodes.
#
#Example 1:
#Input: root = [2,3,1,3,1,null,1]
#Output: 2
#Explanation: The figure above represents the given binary tree. There are three
#paths going from the root node to leaf nodes: the red path [2,3,3], the green
#path [2,1,1], and the path [2,3,1]. Among these paths only red path and green
#path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged
#in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1]
#(palindrome).
#
#Example 2:
#Input: root = [2,1,1,1,3,null,null,null,null,null,1]
#Output: 1
#Explanation: The figure above represents the given binary tree. There are three
#paths going from the root node to leaf nodes: the green path [2,1,1], the path
#[2,1,3,1], and the path [2,1]. Among these paths only the green path is
#pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
#
#Example 3:
#Input: root = [9]
#Output: 1
#
#Constraints:
#    The number of nodes in the tree is in the range [1, 10^5].
#    1 <= Node.val <= 9

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        A path can form palindrome if at most one digit has odd frequency.
        Use bitmask to track parity of digit frequencies.
        """
        def dfs(node: TreeNode, mask: int) -> int:
            if not node:
                return 0

            # Toggle bit for current digit
            mask ^= (1 << node.val)

            # Leaf node: check if at most one bit is set
            if not node.left and not node.right:
                # At most one odd frequency = at most one bit set
                # mask & (mask - 1) clears lowest set bit, result 0 means <= 1 bit set
                return 1 if mask & (mask - 1) == 0 else 0

            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)


class SolutionCounter:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """Using counter to track frequencies"""
        def dfs(node: TreeNode, count: dict) -> int:
            if not node:
                return 0

            count[node.val] = count.get(node.val, 0) + 1

            if not node.left and not node.right:
                # Count odd frequencies
                odd_count = sum(1 for c in count.values() if c % 2 == 1)
                result = 1 if odd_count <= 1 else 0
            else:
                result = dfs(node.left, count) + dfs(node.right, count)

            # Backtrack
            count[node.val] -= 1
            if count[node.val] == 0:
                del count[node.val]

            return result

        return dfs(root, {})


class SolutionIterative:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """Iterative DFS with stack"""
        if not root:
            return 0

        count = 0
        stack = [(root, 0)]

        while stack:
            node, mask = stack.pop()

            mask ^= (1 << node.val)

            if not node.left and not node.right:
                if mask & (mask - 1) == 0:
                    count += 1
            else:
                if node.left:
                    stack.append((node.left, mask))
                if node.right:
                    stack.append((node.right, mask))

        return count
