#77. Combinations
#Medium
#
#Given two integers n and k, return all possible combinations of k numbers chosen
#from the range [1, n].
#
#You may return the answer in any order.
#
#Example 1:
#Input: n = 4, k = 2
#Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#
#Example 2:
#Input: n = 1, k = 1
#Output: [[1]]
#
#Constraints:
#    1 <= n <= 20
#    1 <= k <= n

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Backtracking approach.
        """
        result = []

        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                result.append(path[:])
                return

            # Pruning: need k - len(path) more numbers
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result


class SolutionItertools:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Using itertools.combinations.
        """
        from itertools import combinations
        return [list(c) for c in combinations(range(1, n + 1), k)]


class SolutionIterative:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Iterative approach.
        """
        result = [[]]

        for _ in range(k):
            result = [
                combo + [i]
                for combo in result
                for i in range(combo[-1] + 1 if combo else 1, n + 1)
            ]

        return result


class SolutionLexicographic:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Lexicographic (binary sorted) approach.
        """
        result = []
        nums = list(range(1, k + 1)) + [n + 1]

        j = 0
        while j < k:
            result.append(nums[:k])

            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return result
