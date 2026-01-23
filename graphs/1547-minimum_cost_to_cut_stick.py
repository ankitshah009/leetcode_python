#1547. Minimum Cost to Cut a Stick
#Hard
#
#Given a wooden stick of length n units. The stick is labeled from 0 to n. For
#example, a stick of length 6 is labeled as follows:
#
#Given an integer array cuts where cuts[i] denotes a position you should perform
#a cut at.
#
#You should perform the cuts in order, you can change the order of the cuts as
#you wish.
#
#The cost of one cut is the length of the stick to be cut, the total cost is
#the sum of costs of all cuts. When you cut a stick, it will be split into two
#smaller sticks (i.e. the sum of their lengths is the length of the stick before
#the cut). Please refer to the first example for a better explanation.
#
#Return the minimum total cost of the cuts.
#
#Example 1:
#Input: n = 7, cuts = [1,3,4,5]
#Output: 16
#Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the
#following scenario: cost = 7 + 6 + 4 + 3 = 20.
#The order [3, 5, 1, 4] gives cost = 7 + 4 + 3 + 2 = 16 (minimum).
#
#Example 2:
#Input: n = 9, cuts = [5,6,1,4,2]
#Output: 22
#Explanation: If you try the given cuts ordering the cost will be 25.
#The optimal order is [4, 6, 5, 2, 1] which gives cost = 9 + 4 + 6 + 3 + 2 = 22.
#
#Constraints:
#    2 <= n <= 10^6
#    1 <= cuts.length <= min(n - 1, 100)
#    1 <= cuts[i] <= n - 1
#    All the integers in cuts array are distinct.

from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Interval DP. Similar to matrix chain multiplication.

        Sort cuts and add endpoints 0 and n.
        dp[i][j] = min cost to cut segment between cuts[i] and cuts[j].
        """
        # Add endpoints and sort
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            # No cuts needed between adjacent points
            if j - i <= 1:
                return 0

            # Try each cut position
            min_cost = float('inf')
            for k in range(i + 1, j):
                cost = cuts[j] - cuts[i]  # Cost of this cut
                cost += dp(i, k) + dp(k, j)  # Cost of subproblems
                min_cost = min(min_cost, cost)

            return min_cost

        return dp(0, m - 1)


class SolutionIterative:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Bottom-up DP with tabulation.
        """
        cuts = sorted([0] + cuts + [n])
        m = len(cuts)

        # dp[i][j] = min cost to handle segment from cuts[i] to cuts[j]
        dp = [[0] * m for _ in range(m)]

        # Fill by increasing length
        for length in range(2, m):
            for i in range(m - length):
                j = i + length

                dp[i][j] = float('inf')
                segment_length = cuts[j] - cuts[i]

                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + segment_length)

        return dp[0][m - 1]


class SolutionOptimized:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Optimized with early termination.
        """
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        INF = float('inf')
        dp = [[INF] * m for _ in range(m)]

        # Base case: adjacent cuts need no cost
        for i in range(m - 1):
            dp[i][i + 1] = 0

        # Fill by length
        for gap in range(2, m):
            for i in range(m - gap):
                j = i + gap
                length = cuts[j] - cuts[i]

                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + length)

        return dp[0][m - 1]


class SolutionExplained:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Detailed explanation of the interval DP approach.

        Key insight: The order of cuts matters because each cut costs
        the current length of the stick segment.

        This is similar to optimal BST or matrix chain multiplication.

        State: dp[i][j] = minimum cost to make all cuts between
               cuts[i] and cuts[j] (these are the endpoints).

        Transition: Try each possible first cut k, where i < k < j.
        Cost = (cuts[j] - cuts[i]) + dp[i][k] + dp[k][j]

        The first term is the cost of making cut k.
        The remaining terms are costs for the two resulting segments.
        """
        # Add boundary points
        points = sorted([0] + cuts + [n])
        m = len(points)

        # Memoization table
        memo = {}

        def solve(left: int, right: int) -> int:
            if right - left <= 1:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            segment_len = points[right] - points[left]
            result = float('inf')

            for k in range(left + 1, right):
                cost = segment_len + solve(left, k) + solve(k, right)
                result = min(result, cost)

            memo[(left, right)] = result
            return result

        return solve(0, m - 1)
