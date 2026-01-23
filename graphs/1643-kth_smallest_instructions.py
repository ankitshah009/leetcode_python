#1643. Kth Smallest Instructions
#Hard
#
#Bob is standing at cell (0, 0), and he wants to reach destination: (row, column).
#He can only travel right and down. You are going to help Bob by providing
#instructions for him to reach destination.
#
#The instructions are represented as a string, where each character is either:
#- 'H', meaning move horizontally (go right), or
#- 'V', meaning move vertically (go down).
#
#Multiple instructions will lead Bob to destination. For example, if destination
#is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.
#
#However, Bob is very picky. Bob has a lucky number k, and he wants the kth
#lexicographically smallest instructions that will lead him to destination.
#k is 1-indexed.
#
#Given an integer array destination and an integer k, return the kth
#lexicographically smallest instructions that will lead Bob to destination.
#
#Example 1:
#Input: destination = [2,3], k = 1
#Output: "HHHVV"
#Explanation: All the instructions are:
#["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"]
#The 1st smallest is "HHHVV".
#
#Example 2:
#Input: destination = [2,3], k = 2
#Output: "HHVHV"
#
#Example 3:
#Input: destination = [2,3], k = 3
#Output: "HHVVH"
#
#Constraints:
#    destination.length == 2
#    1 <= row, column <= 15
#    1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b.

from typing import List
from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        """
        Greedy with combinatorics.

        At each step, decide whether to use 'H' or 'V':
        - Count how many strings start with 'H' (using remaining H's and V's)
        - If k <= that count, use 'H'
        - Otherwise, use 'V' and update k
        """
        v, h = destination  # v = vertical moves, h = horizontal moves
        result = []

        for _ in range(h + v):
            if h == 0:
                result.append('V')
                v -= 1
            elif v == 0:
                result.append('H')
                h -= 1
            else:
                # Count strings starting with 'H' = C(h-1+v, v)
                count_h = comb(h - 1 + v, v)

                if k <= count_h:
                    result.append('H')
                    h -= 1
                else:
                    result.append('V')
                    k -= count_h
                    v -= 1

        return ''.join(result)


class SolutionDP:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        """
        DP approach with Pascal's triangle for combinations.
        """
        v, h = destination
        total = h + v

        # Precompute combinations using Pascal's triangle
        C = [[0] * (total + 1) for _ in range(total + 1)]
        for i in range(total + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

        result = []

        for _ in range(total):
            if h == 0:
                result.append('V')
                v -= 1
            elif v == 0:
                result.append('H')
                h -= 1
            else:
                # Paths starting with H = C[h-1+v][v]
                count_h = C[h - 1 + v][v]

                if k <= count_h:
                    result.append('H')
                    h -= 1
                else:
                    result.append('V')
                    k -= count_h
                    v -= 1

        return ''.join(result)


class SolutionRecursive:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        """
        Recursive approach.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def count_paths(h: int, v: int) -> int:
            """Count paths with h horizontal and v vertical moves."""
            if h == 0 or v == 0:
                return 1
            return count_paths(h - 1, v) + count_paths(h, v - 1)

        v, h = destination
        result = []

        while h > 0 or v > 0:
            if h == 0:
                result.append('V')
                v -= 1
            elif v == 0:
                result.append('H')
                h -= 1
            else:
                paths_with_h = count_paths(h - 1, v)
                if k <= paths_with_h:
                    result.append('H')
                    h -= 1
                else:
                    result.append('V')
                    k -= paths_with_h
                    v -= 1

        return ''.join(result)
