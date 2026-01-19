#272. Closest Binary Search Tree Value II
#Hard
#
#Given the root of a binary search tree, a target value, and an integer k, return
#the k values in the BST that are closest to the target. You may return the answer
#in any order.
#
#You are guaranteed to have only one unique set of k values in the BST that are
#closest to the target.
#
#Example 1:
#Input: root = [4,2,5,1,3], target = 3.714286, k = 2
#Output: [4,3]
#
#Example 2:
#Input: root = [1], target = 0.000000, k = 1
#Output: [1]
#
#Constraints:
#    The number of nodes in the tree is n.
#    1 <= k <= n <= 10^4
#    0 <= Node.val <= 10^9
#    -10^9 <= target <= 10^9
#
#Follow up: Assume that the BST is balanced. Could you solve it in less than O(n)
#runtime (where n = total nodes)?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
from collections import deque

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # Inorder traversal gives sorted order
        # Use sliding window of size k
        result = deque()

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if len(result) < k:
                result.append(node.val)
            elif abs(node.val - target) < abs(result[0] - target):
                result.popleft()
                result.append(node.val)
            else:
                # All remaining nodes are further from target
                return

            inorder(node.right)

        inorder(root)
        return list(result)

    # Max-heap approach
    def closestKValuesHeap(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # Use max heap of size k (negate distance for max heap behavior)
        heap = []

        def dfs(node):
            if not node:
                return

            dist = abs(node.val - target)

            if len(heap) < k:
                heapq.heappush(heap, (-dist, node.val))
            elif dist < -heap[0][0]:
                heapq.heapreplace(heap, (-dist, node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return [val for _, val in heap]

    # Two stack approach for O(k + log n) time with balanced BST
    def closestKValuesTwoStacks(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        predecessors = []  # Stack for values <= target (reverse inorder)
        successors = []    # Stack for values > target (inorder)

        # Initialize stacks
        node = root
        while node:
            if node.val <= target:
                predecessors.append(node)
                node = node.right
            else:
                successors.append(node)
                node = node.left

        def get_predecessor():
            if not predecessors:
                return None
            node = predecessors.pop()
            val = node.val
            node = node.left
            while node:
                predecessors.append(node)
                node = node.right
            return val

        def get_successor():
            if not successors:
                return None
                node = successors.pop()
            val = node.val
            node = node.right
            while node:
                successors.append(node)
                node = node.left
            return val

        result = []
        pred = get_predecessor()
        succ = get_successor()

        for _ in range(k):
            if pred is None:
                result.append(succ)
                succ = get_successor()
            elif succ is None:
                result.append(pred)
                pred = get_predecessor()
            elif abs(pred - target) <= abs(succ - target):
                result.append(pred)
                pred = get_predecessor()
            else:
                result.append(succ)
                succ = get_successor()

        return result
