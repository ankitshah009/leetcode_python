#1621. Number of Sets of K Non-Overlapping Line Segments
#Medium
#
#Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i,
#find the number of ways we can draw exactly k non-overlapping line segments
#such that each segment covers two or more points. The endpoints of each segment
#must have integral coordinates. The k line segments do not have to cover all
#n points, and they are allowed to share endpoints.
#
#Return the number of ways we can draw k non-overlapping line segments. Since
#this number can be huge, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 4, k = 2
#Output: 5
#Explanation: The two line segments are shown in red and blue.
#The 5 ways are:
#[[0,1],[2,3]], [[0,2],[3,3]], [[0,1],[1,3]], [[0,2],[2,3]], [[1,2],[2,3]]
#Note: lines can share endpoints.
#
#Example 2:
#Input: n = 3, k = 1
#Output: 3
#Explanation: The 3 ways are [[0,1]], [[0,2]], [[1,2]].
#
#Example 3:
#Input: n = 30, k = 7
#Output: 796297179
#
#Constraints:
#    2 <= n <= 1000
#    1 <= k <= n-1

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        Key insight: This is equivalent to choosing 2k points from n+k-1 points
        (using stars and bars / combinatorics).

        The answer is C(n + k - 1, 2k) where C is combination.

        Alternative DP approach:
        dp[i][j][0] = ways to use points 0..i to form j segments, not in a segment
        dp[i][j][1] = ways to use points 0..i to form j segments, currently in segment
        """
        MOD = 10**9 + 7

        # Combinatorics solution: C(n + k - 1, 2k)
        # Using Pascal's identity
        total = n + k - 1
        choose = 2 * k

        # Compute C(total, choose) using dynamic programming
        # C[i][j] = C(i, j)
        C = [[0] * (choose + 1) for _ in range(total + 1)]

        for i in range(total + 1):
            C[i][0] = 1
            for j in range(1, min(i, choose) + 1):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        return C[total][choose]


class SolutionDP:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        DP solution with state (position, segments, in_segment).
        """
        MOD = 10**9 + 7

        # dp[i][j][s] = ways to cover points 0..i with j complete segments
        # s = 0: not currently in a segment
        # s = 1: currently in a segment

        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][0] = 1  # At point 0, 0 segments, not in segment
        dp[0][0][1] = 1  # At point 0, start a segment

        for i in range(1, n):
            for j in range(k + 1):
                # Not in segment at point i
                # Can come from: not in segment at i-1, or just ended segment at i-1
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD

                # In segment at point i
                if j > 0:
                    # Either continue segment from i-1, or start new segment
                    # Start new: was not in segment at i-1
                    # Continue: was in segment at i-1 (might end here or continue)
                    dp[i][j][1] = (dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j][1]) % MOD
                else:
                    # j=0, can only start first segment
                    dp[i][0][1] = (dp[i-1][0][0] + dp[i-1][0][1]) % MOD

        # Answer: k segments completed, either still in or not
        return (dp[n-1][k][0] + dp[n-1][k][1]) % MOD


class SolutionCombinatorics:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        Pure combinatorics using modular inverse.
        Answer = C(n + k - 1, 2k)
        """
        MOD = 10**9 + 7

        def mod_inverse(a, mod):
            return pow(a, mod - 2, mod)

        def comb(n, r):
            if r > n or r < 0:
                return 0
            if r == 0 or r == n:
                return 1

            num = 1
            den = 1
            for i in range(r):
                num = num * (n - i) % MOD
                den = den * (i + 1) % MOD

            return num * mod_inverse(den, MOD) % MOD

        return comb(n + k - 1, 2 * k)
