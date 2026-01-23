#22. Generate Parentheses
#Medium
#
#Given n pairs of parentheses, write a function to generate all combinations of
#well-formed parentheses.
#
#Example 1:
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#
#Example 2:
#Input: n = 1
#Output: ["()"]
#
#Constraints:
#    1 <= n <= 8

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Backtracking with open/close count tracking.
        """
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result


class SolutionDP:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Dynamic Programming approach.
        dp[i] contains all valid parentheses combinations of length i.
        For each combination: ( + dp[j] + ) + dp[i-j-1]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']

        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        dp[i].append('(' + left + ')' + right)

        return dp[n]


class SolutionIterative:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Iterative BFS-like approach.
        """
        if n == 0:
            return []

        # (string, open_count, close_count)
        queue = [('', 0, 0)]
        result = []

        while queue:
            current, open_count, close_count = queue.pop(0)

            if len(current) == 2 * n:
                result.append(current)
                continue

            if open_count < n:
                queue.append((current + '(', open_count + 1, close_count))

            if close_count < open_count:
                queue.append((current + ')', open_count, close_count + 1))

        return result


class SolutionClosure:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Closure number approach.
        """
        if n == 0:
            return ['']

        result = []

        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    result.append('(' + left + ')' + right)

        return result
