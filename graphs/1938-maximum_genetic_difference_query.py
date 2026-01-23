#1938. Maximum Genetic Difference Query
#Hard
#
#There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's
#number denotes its unique genetic value (i.e. the genetic value of node i is
#i). The genetic difference between two genetic values is defined as the
#bitwise-XOR of their values.
#
#You are given the integer array parents, where parents[i] is the parent for
#node i. If node x is the root of the tree, then parents[x] == -1.
#
#You are given the array queries where queries[i] = [node_i, val_i]. For each
#query i, find the maximum genetic difference between val_i and p_i, where p_i
#is any node on the path between node_i and the root (including node_i and the
#root).
#
#Return an array ans where ans[i] is the answer to the ith query.
#
#Example 1:
#Input: parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
#Output: [2,3,7]
#
#Constraints:
#    2 <= parents.length <= 10^5
#    0 <= parents[i] <= parents.length - 1 for i != root
#    parents[root] == -1
#    1 <= queries.length <= 3 * 10^4
#    0 <= node_i <= parents.length - 1
#    0 <= val_i <= 2 * 10^5

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        """
        DFS on tree with Trie for XOR queries.
        Add node to trie when entering, remove when leaving.
        """
        n = len(parents)
        MAX_BIT = 17  # log2(2 * 10^5)

        # Build tree
        children = defaultdict(list)
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # Group queries by node
        query_map = defaultdict(list)
        for i, (node, val) in enumerate(queries):
            query_map[node].append((val, i))

        result = [0] * len(queries)

        # Trie operations
        trie_root = TrieNode()

        def insert(num):
            node = trie_root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.count += 1

        def remove(num):
            node = trie_root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                node = node.children[bit]
                node.count -= 1

        def max_xor(val):
            node = trie_root
            result = 0
            for i in range(MAX_BIT, -1, -1):
                bit = (val >> i) & 1
                opposite = 1 - bit

                if node.children[opposite] and node.children[opposite].count > 0:
                    result |= (1 << i)
                    node = node.children[opposite]
                elif node.children[bit] and node.children[bit].count > 0:
                    node = node.children[bit]
                else:
                    break

            return result

        # DFS
        def dfs(node):
            insert(node)

            # Answer queries at this node
            for val, idx in query_map[node]:
                result[idx] = max_xor(val)

            # Visit children
            for child in children[node]:
                dfs(child)

            remove(node)

        dfs(root)
        return result
