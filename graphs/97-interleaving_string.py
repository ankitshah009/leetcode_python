#97. Interleaving String
#Medium
#
#Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
#s1 and s2.
#
#An interleaving of two strings s and t is a configuration where s and t are
#divided into n and m substrings respectively, such that:
#- s = s1 + s2 + ... + sn
#- t = t1 + t2 + ... + tm
#- |n - m| <= 1
#- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + ...
#
#Example 1:
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#Output: true
#
#Example 2:
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#Output: false
#
#Example 3:
#Input: s1 = "", s2 = "", s3 = ""
#Output: true
#
#Constraints:
#    0 <= s1.length, s2.length <= 100
#    0 <= s3.length <= 200
#    s1, s2, and s3 consist of lowercase English letters.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        2D DP - O(m*n) time and space.
        """
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        # dp[i][j] = can s1[:i] and s2[:j] interleave to form s3[:i+j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Initialize first row (only using s2)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Initialize first column (only using s1)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill rest
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Take from s1 or s2
                dp[i][j] = (
                    (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[m][n]


class SolutionSpaceOptimized:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        1D DP - O(n) space.
        """
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        # Use shorter string for dp array
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False] * (n + 1)
        dp[0] = True

        # Initialize first row
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill row by row
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[n]


class SolutionMemo:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Top-down with memoization.
        """
        from functools import lru_cache

        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            k = i + j

            if k == len(s3):
                return True

            result = False

            if i < len(s1) and s1[i] == s3[k]:
                result = dp(i + 1, j)

            if not result and j < len(s2) and s2[j] == s3[k]:
                result = dp(i, j + 1)

            return result

        return dp(0, 0)


class SolutionBFS:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        BFS approach.
        """
        from collections import deque

        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        visited = set()
        queue = deque([(0, 0)])

        while queue:
            i, j = queue.popleft()
            k = i + j

            if k == len(s3):
                return True

            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i < m and s1[i] == s3[k]:
                queue.append((i + 1, j))

            if j < n and s2[j] == s3[k]:
                queue.append((i, j + 1))

        return False
