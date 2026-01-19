#279. Perfect Squares
#Medium
#
#Given an integer n, return the least number of perfect square numbers that
#sum to n.
#
#A perfect square is an integer that is the square of an integer; in other words,
#it is the product of some integer with itself. For example, 1, 4, 9, and 16 are
#perfect squares while 3 and 11 are not.
#
#Example 1:
#Input: n = 12
#Output: 3
#Explanation: 12 = 4 + 4 + 4
#
#Example 2:
#Input: n = 13
#Output: 2
#Explanation: 13 = 4 + 9
#
#Constraints:
#    1 <= n <= 10^4

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        """Dynamic programming - O(n * sqrt(n))"""
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Precompute squares
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]


class SolutionBFS:
    """BFS approach - find shortest path"""

    def numSquares(self, n: int) -> int:
        # Precompute squares
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        queue = deque([(n, 0)])  # (remaining, count)
        visited = {n}

        while queue:
            remaining, count = queue.popleft()

            for sq in squares:
                new_remaining = remaining - sq

                if new_remaining == 0:
                    return count + 1

                if new_remaining > 0 and new_remaining not in visited:
                    visited.add(new_remaining)
                    queue.append((new_remaining, count + 1))

        return -1


class SolutionMath:
    """
    Mathematical approach using Lagrange's four-square theorem.
    Every positive integer can be expressed as sum of four or fewer squares.
    """

    def numSquares(self, n: int) -> int:
        import math

        # Check if perfect square
        if int(math.sqrt(n)) ** 2 == n:
            return 1

        # Check if sum of two squares
        for i in range(1, int(math.sqrt(n)) + 1):
            remainder = n - i * i
            if int(math.sqrt(remainder)) ** 2 == remainder:
                return 2

        # Check if n = 4^a * (8b + 7) (Legendre's three-square theorem)
        # Then n requires exactly 4 squares
        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        return 3


class SolutionMemo:
    """Memoization approach"""

    def numSquares(self, n: int) -> int:
        from functools import lru_cache

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        @lru_cache(maxsize=None)
        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining in squares:
                return 1

            min_count = float('inf')
            for sq in squares:
                if sq > remaining:
                    break
                min_count = min(min_count, 1 + dp(remaining - sq))

            return min_count

        return dp(n)
