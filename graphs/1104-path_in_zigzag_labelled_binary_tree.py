#1104. Path In Zigzag Labelled Binary Tree
#Medium
#
#In an infinite binary tree where every node has two children, the nodes
#are labelled in row order.
#
#In the odd numbered rows (ie., the first, third, fifth,...), the labelling
#is left to right, while in the even numbered rows (second, fourth, sixth,...),
#the labelling is right to left.
#
#Given the label of a node in this tree, return the labels in the path from
#the root of the tree to the node with that label.
#
#Example 1:
#Input: label = 14
#Output: [1,3,4,14]
#
#Example 2:
#Input: label = 26
#Output: [1,2,6,10,26]
#
#Constraints:
#    1 <= label <= 10^6

from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        Find level, then trace path to root.
        Account for zigzag by reflecting label within level.
        """
        # Find level (1-indexed)
        level = 1
        while (1 << level) <= label:
            level += 1

        result = []

        while label >= 1:
            result.append(label)

            # Get parent in normal tree
            parent = label // 2

            # But since we're in zigzag, we need to reflect
            # Level start: 2^(level-1), Level end: 2^level - 1
            # Reflected label = start + end - label
            level -= 1
            if level >= 1:
                level_start = 1 << (level - 1)
                level_end = (1 << level) - 1
                parent = level_start + level_end - parent

            label = parent

        return result[::-1]


class SolutionAlternative:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """Track level and reflect as needed"""
        import math

        level = int(math.log2(label)) + 1
        result = [0] * level

        while label >= 1:
            result[level - 1] = label

            # Move to parent level
            level -= 1
            if level == 0:
                break

            # Calculate parent
            # In normal tree, parent would be label // 2
            # But every other level is reversed
            parent_normal = label // 2
            # Reflect in parent's level
            level_start = 1 << (level - 1)
            level_end = (1 << level) - 1
            label = level_start + level_end - parent_normal

        return result


class SolutionIterative:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """Clear iterative approach"""
        result = []
        node = label

        while node > 0:
            result.append(node)
            node //= 2

        result = result[::-1]

        # Now fix the zigzag
        for i in range(len(result)):
            level = i + 1
            # Odd levels (1, 3, 5...) are left-to-right - keep as is
            # But we need to check parity based on total levels
            should_flip = (len(result) - level) % 2 == 1

            if should_flip:
                level_start = 1 << (level - 1)
                level_end = (1 << level) - 1
                result[i] = level_start + level_end - result[i]

        return result
