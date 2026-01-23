#40. Combination Sum II
#Medium
#
#Given a collection of candidate numbers (candidates) and a target number (target),
#find all unique combinations in candidates where the candidate numbers sum to
#target.
#
#Each number in candidates may only be used once in the combination.
#
#Note: The solution set must not contain duplicate combinations.
#
#Example 1:
#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
#
#Example 2:
#Input: candidates = [2,5,2,1,2], target = 5
#Output: [[1,2,2],[5]]
#
#Constraints:
#    1 <= candidates.length <= 100
#    1 <= candidates[i] <= 50
#    1 <= target <= 30

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking with duplicate skipping.
        """
        result = []
        candidates.sort()

        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break  # Pruning

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result


class SolutionCounter:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Using Counter to handle duplicates.
        """
        from collections import Counter

        result = []
        counter = Counter(candidates)
        unique = sorted(counter.keys())

        def backtrack(idx: int, remaining: int, path: List[int]):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(idx, len(unique)):
                num = unique[i]

                if num > remaining:
                    break

                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(i, remaining - num, path)
                    path.pop()
                    counter[num] += 1

        backtrack(0, target, [])
        return result


class SolutionIterative:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Iterative with stack.
        """
        candidates.sort()
        result = []
        stack = [(0, target, [])]

        while stack:
            start, remaining, path = stack.pop()

            if remaining == 0:
                result.append(path)
                continue

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                stack.append((i + 1, remaining - candidates[i], path + [candidates[i]]))

        return result
