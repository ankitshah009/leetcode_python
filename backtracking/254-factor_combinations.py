#254. Factor Combinations
#Medium
#
#Numbers can be regarded as the product of their factors.
#
#For example, 8 = 2 x 2 x 2 = 2 x 4.
#
#Given an integer n, return all possible combinations of its factors. You may
#return the answer in any order.
#
#Note that the factors should be in the range [2, n - 1].
#
#Example 1:
#Input: n = 1
#Output: []
#
#Example 2:
#Input: n = 12
#Output: [[2,6],[3,4],[2,2,3]]
#
#Example 3:
#Input: n = 37
#Output: []
#
#Constraints:
#    1 <= n <= 10^7

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, path):
            if target == 1:
                if len(path) > 1:  # Exclude [n] itself
                    result.append(path[:])
                return

            for factor in range(start, int(target ** 0.5) + 1):
                if target % factor == 0:
                    path.append(factor)
                    backtrack(factor, target // factor, path)
                    path.pop()

            # Include target itself as the last factor
            if target >= start:
                path.append(target)
                backtrack(target, 1, path)
                path.pop()

        backtrack(2, n, [])
        return result

    # Alternative cleaner approach
    def getFactorsAlt(self, n: int) -> List[List[int]]:
        def dfs(start, target):
            if target == 1:
                return [[]]

            result = []
            for factor in range(start, int(target ** 0.5) + 1):
                if target % factor == 0:
                    for rest in dfs(factor, target // factor):
                        result.append([factor] + rest)

            # Add target itself as a single factor if valid
            if target >= start and target != n:
                result.append([target])

            return result

        return dfs(2, n)

    # Iterative BFS approach
    def getFactorsIterative(self, n: int) -> List[List[int]]:
        if n <= 1:
            return []

        from collections import deque

        result = []
        queue = deque([(2, n, [])])  # (start, remaining, path)

        while queue:
            start, remaining, path = queue.popleft()

            for factor in range(start, int(remaining ** 0.5) + 1):
                if remaining % factor == 0:
                    new_path = path + [factor]
                    quotient = remaining // factor
                    result.append(new_path + [quotient])
                    queue.append((factor, quotient, new_path))

        return result
