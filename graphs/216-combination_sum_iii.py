#216. Combination Sum III
#Medium
#
#Find all valid combinations of k numbers that sum up to n such that the
#following conditions are true:
#    Only numbers 1 through 9 are used.
#    Each number is used at most once.
#
#Return a list of all possible valid combinations. The list must not contain
#the same combination twice, and the combinations may be returned in any order.
#
#Example 1:
#Input: k = 3, n = 7
#Output: [[1,2,4]]
#Explanation:
#1 + 2 + 4 = 7. There are no other valid combinations.
#
#Example 2:
#Input: k = 3, n = 9
#Output: [[1,2,6],[1,3,5],[2,3,4]]
#Explanation:
#1 + 2 + 6 = 9
#1 + 3 + 5 = 9
#2 + 3 + 4 = 9
#There are no other valid combinations.
#
#Example 3:
#Input: k = 4, n = 1
#Output: []
#Explanation: There are no valid combinations.
#
#Constraints:
#    2 <= k <= 9
#    1 <= n <= 60

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining, path):
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return

            # Pruning: not enough numbers left or sum too large
            if remaining < 0 or len(path) + (10 - start) < k:
                return

            for num in range(start, 10):
                if num > remaining:  # Pruning
                    break

                path.append(num)
                backtrack(num + 1, remaining - num, path)
                path.pop()

        backtrack(1, n, [])
        return result


class SolutionItertools:
    """Using itertools combinations"""

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations

        return [list(c) for c in combinations(range(1, 10), k) if sum(c) == n]


class SolutionBitMask:
    """Bit manipulation to enumerate all combinations"""

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        # Iterate through all subsets of {1, 2, ..., 9}
        for mask in range(1 << 9):
            if bin(mask).count('1') == k:
                combo = [i + 1 for i in range(9) if mask & (1 << i)]
                if sum(combo) == n:
                    result.append(combo)

        return result


class SolutionMemo:
    """Memoized recursion"""

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def solve(start, count, target):
            if count == 0:
                return [()] if target == 0 else []

            if target <= 0 or start > 9:
                return []

            result = []

            # Include current number
            for combo in solve(start + 1, count - 1, target - start):
                result.append((start,) + combo)

            # Exclude current number
            result.extend(solve(start + 1, count, target))

            return result

        return [list(combo) for combo in solve(1, k, n)]
