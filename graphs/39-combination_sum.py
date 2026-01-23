#39. Combination Sum
#Medium
#
#Given an array of distinct integers candidates and a target integer target,
#return a list of all unique combinations of candidates where the chosen numbers
#sum to target. You may return the combinations in any order.
#
#The same number may be chosen from candidates an unlimited number of times. Two
#combinations are unique if the frequency of at least one of the chosen numbers
#is different.
#
#The test cases are generated such that the number of unique combinations that
#sum up to target is less than 150 combinations for the given input.
#
#Example 1:
#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]
#
#Example 2:
#Input: candidates = [2,3,5], target = 8
#Output: [[2,2,2,2],[2,3,3],[3,5]]
#
#Example 3:
#Input: candidates = [2], target = 1
#Output: []
#
#Constraints:
#    1 <= candidates.length <= 30
#    2 <= candidates[i] <= 40
#    All elements of candidates are distinct.
#    1 <= target <= 40

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking with pruning.
        """
        result = []
        candidates.sort()

        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # Pruning - sorted, so all remaining will be larger

                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # i, not i+1 (reuse allowed)
                path.pop()

        backtrack(0, target, [])
        return result


class SolutionDP:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Dynamic Programming approach.
        dp[i] = all combinations that sum to i.
        """
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for candidate in candidates:
            for i in range(candidate, target + 1):
                for combo in dp[i - candidate]:
                    dp[i].append(combo + [candidate])

        return dp[target]


class SolutionIterative:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Iterative BFS-like approach.
        """
        candidates.sort()
        result = []
        stack = [(0, target, [])]  # (start_index, remaining, current_path)

        while stack:
            start, remaining, path = stack.pop()

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                new_path = path + [candidates[i]]

                if candidates[i] == remaining:
                    result.append(new_path)
                else:
                    stack.append((i, remaining - candidates[i], new_path))

        return result


class SolutionMemo:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Memoization approach.
        """
        from functools import lru_cache

        candidates.sort()

        @lru_cache(maxsize=None)
        def dp(start: int, remaining: int) -> List[tuple]:
            if remaining == 0:
                return [()]

            result = []

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                for combo in dp(i, remaining - candidates[i]):
                    result.append((candidates[i],) + combo)

            return result

        return [list(combo) for combo in dp(0, target)]
