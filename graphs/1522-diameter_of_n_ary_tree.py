#1522. Diameter of N-Ary Tree
#Medium
#
#Given a root of an N-ary tree, you need to compute the length of the diameter
#of the tree.
#
#The diameter of an N-ary tree is the length of the longest path between any
#two nodes in the tree. This path may or may not pass through the root.
#
#(Nary-Tree input serialization is represented in their level order traversal,
#each group of children is separated by the null value.)
#
#Example 1:
#Input: root = [1,null,3,2,4,null,5,6]
#Output: 3
#Explanation: Diameter is shown in red color.
#
#Example 2:
#Input: root = [1,null,2,null,3,4,null,5,null,6]
#Output: 4
#
#Example 3:
#Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#Output: 7
#
#Constraints:
#    The depth of the n-ary tree is less than or equal to 1000.
#    The total number of nodes is between [1, 10^4].

from typing import Optional, List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        DFS: for each node, the longest path passing through it is
        sum of two longest paths to leaf descendants.
        Track maximum diameter seen.
        """
        self.max_diameter = 0

        def dfs(node: 'Node') -> int:
            """Returns height of subtree (max depth to any leaf)"""
            if not node:
                return 0

            if not node.children:
                return 0

            # Get heights of all children
            heights = []
            for child in node.children:
                heights.append(dfs(child) + 1)

            # Sort to get two largest
            heights.sort(reverse=True)

            # Diameter through this node
            if len(heights) >= 2:
                self.max_diameter = max(self.max_diameter, heights[0] + heights[1])
            else:
                self.max_diameter = max(self.max_diameter, heights[0])

            return heights[0]

        dfs(root)
        return self.max_diameter


class SolutionOptimized:
    def diameter(self, root: 'Node') -> int:
        """
        Optimized: only track two largest heights, no sorting needed.
        """
        self.result = 0

        def depth(node: 'Node') -> int:
            if not node:
                return 0

            # Track top 2 depths
            max1 = max2 = 0

            for child in node.children:
                d = depth(child) + 1
                if d >= max1:
                    max2 = max1
                    max1 = d
                elif d > max2:
                    max2 = d

            # Diameter through this node
            self.result = max(self.result, max1 + max2)

            return max1

        depth(root)
        return self.result


class SolutionIterative:
    def diameter(self, root: 'Node') -> int:
        """
        Iterative post-order traversal.
        """
        if not root:
            return 0

        max_diameter = 0
        heights = {}

        # Post-order using stack
        stack = [(root, False)]

        while stack:
            node, processed = stack.pop()

            if processed:
                # All children processed, compute height
                child_heights = [heights.get(child, 0) + 1 for child in node.children]

                if len(child_heights) >= 2:
                    child_heights.sort(reverse=True)
                    max_diameter = max(max_diameter, child_heights[0] + child_heights[1])
                elif len(child_heights) == 1:
                    max_diameter = max(max_diameter, child_heights[0])

                heights[node] = max(child_heights) if child_heights else 0
            else:
                stack.append((node, True))
                for child in node.children:
                    stack.append((child, False))

        return max_diameter


class SolutionBFS:
    def diameter(self, root: 'Node') -> int:
        """
        Two BFS: find farthest node from root, then farthest from that node.
        """
        from collections import deque

        if not root:
            return 0

        # Build graph (undirected for BFS)
        graph = {}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            graph[node] = node.children[:]
            for child in node.children:
                if child not in graph:
                    graph[child] = []
                graph[child].append(node)
                queue.append(child)

        def bfs_farthest(start: 'Node') -> tuple:
            """Find farthest node and its distance"""
            visited = {start}
            queue = deque([(start, 0)])
            farthest = start
            max_dist = 0

            while queue:
                node, dist = queue.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest = node

                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

            return farthest, max_dist

        # Find one end of diameter
        end1, _ = bfs_farthest(root)

        # Find other end and diameter
        _, diameter = bfs_farthest(end1)

        return diameter
