#1707. Maximum XOR With an Element From Array
#Hard
#
#You are given an array nums consisting of non-negative integers. You are also
#given a queries array, where queries[i] = [xi, mi].
#
#The answer to the ith query is the maximum bitwise XOR value of xi and any
#element of nums that does not exceed mi. If all elements in nums are larger
#than mi, then the answer is -1.
#
#Return an integer array answer where answer.length == queries.length and
#answer[i] is the answer to the ith query.
#
#Example 1:
#Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
#Output: [3,3,7]
#
#Example 2:
#Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
#Output: [15,-1,5]
#
#Constraints:
#    1 <= nums.length, queries.length <= 10^5
#    queries[i].length == 2
#    0 <= nums[i], xi, mi <= 10^9

from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Offline processing with Trie.
        Sort nums and queries by limit, process in order.
        """
        # Sort nums
        nums.sort()

        # Add index to queries and sort by limit
        indexed_queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        indexed_queries.sort(key=lambda q: q[1])

        result = [-1] * len(queries)
        root = TrieNode()
        num_idx = 0
        n = len(nums)

        for x, m, query_idx in indexed_queries:
            # Add all nums <= m to trie
            while num_idx < n and nums[num_idx] <= m:
                self.insert(root, nums[num_idx])
                num_idx += 1

            # Find max XOR if trie is not empty
            if num_idx > 0:
                result[query_idx] = self.max_xor(root, x)

        return result

    def insert(self, root: TrieNode, num: int):
        node = root
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def max_xor(self, root: TrieNode, num: int) -> int:
        node = root
        result = 0
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite direction for max XOR
            want = 1 - bit
            if node.children[want]:
                result |= (1 << i)
                node = node.children[want]
            elif node.children[bit]:
                node = node.children[bit]
            else:
                return -1
        return result


class SolutionBruteForce:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Brute force - O(n * q) - for small inputs.
        """
        result = []

        for x, m in queries:
            max_xor = -1
            for num in nums:
                if num <= m:
                    max_xor = max(max_xor, x ^ num)
            result.append(max_xor)

        return result
