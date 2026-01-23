#1803. Count Pairs With XOR in a Range
#Hard
#
#Given a (0-indexed) integer array nums and two integers low and high, return
#the number of nice pairs.
#
#A nice pair is a pair (i, j) where 0 <= i < j < nums.length and
#low <= (nums[i] XOR nums[j]) <= high.
#
#Example 1:
#Input: nums = [1,4,2,7], low = 2, high = 6
#Output: 6
#
#Example 2:
#Input: nums = [9,8,4,2,1], low = 5, high = 14
#Output: 8
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    1 <= nums[i] <= 2 * 10^4
#    1 <= low <= high <= 2 * 10^4

from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        """
        Use Trie to count pairs with XOR < limit.
        Answer = count(XOR <= high) - count(XOR < low)
        """
        def count_less_than(limit: int) -> int:
            """Count pairs with XOR < limit."""
            root = TrieNode()
            count = 0

            for num in nums:
                # Query how many existing numbers XOR with num give < limit
                node = root
                for i in range(14, -1, -1):
                    num_bit = (num >> i) & 1
                    limit_bit = (limit >> i) & 1

                    if limit_bit == 1:
                        # If we go same as num_bit, XOR gives 0 < 1
                        # Count all in that subtree
                        if node.children[num_bit]:
                            count += node.children[num_bit].count
                        # Continue with XOR = 1 (opposite bit)
                        node = node.children[1 - num_bit]
                    else:
                        # Must follow num_bit to keep XOR = 0
                        node = node.children[num_bit]

                    if not node:
                        break

                # Insert current number
                node = root
                for i in range(14, -1, -1):
                    bit = (num >> i) & 1
                    if not node.children[bit]:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                    node.count += 1

            return count

        return count_less_than(high + 1) - count_less_than(low)


class SolutionBruteForce:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        """
        Brute force O(n^2) for verification.
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                xor_val = nums[i] ^ nums[j]
                if low <= xor_val <= high:
                    count += 1
        return count
