#960. Delete Columns to Make Sorted III
#Hard
#
#You are given an array of n strings strs, all of the same length.
#
#We may choose any deletion indices, and we delete all the characters in those
#indices for each string.
#
#Suppose we chose a set of deletion indices answer such that after deletions,
#each remaining column of strs is in non-decreasing sorted order.
#
#Return the minimum possible value of answer.length.
#
#Example 1:
#Input: strs = ["babca","bbazb"]
#Output: 3
#Explanation: After deleting columns 0, 1, and 4, each row is non-decreasing.
#
#Example 2:
#Input: strs = ["edcba"]
#Output: 4
#
#Example 3:
#Input: strs = ["ghi","def","abc"]
#Output: 0
#
#Constraints:
#    n == strs.length
#    1 <= n <= 100
#    1 <= strs[i].length <= 100
#    strs[i] consists of lowercase English letters.

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Find longest increasing subsequence of columns.
        Answer = total columns - LIS length.
        """
        n = len(strs)
        m = len(strs[0])

        # dp[i] = length of longest valid subsequence ending at column i
        dp = [1] * m

        for i in range(1, m):
            for j in range(i):
                # Check if column j can come before column i
                if all(strs[k][j] <= strs[k][i] for k in range(n)):
                    dp[i] = max(dp[i], dp[j] + 1)

        return m - max(dp)


class SolutionExplicit:
    """More explicit comparison"""

    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        def is_valid(j, i):
            """Check if column j can precede column i."""
            for row in strs:
                if row[j] > row[i]:
                    return False
            return True

        # LIS of columns
        dp = [1] * m

        for i in range(m):
            for j in range(i):
                if is_valid(j, i):
                    dp[i] = max(dp[i], dp[j] + 1)

        return m - max(dp)


class SolutionMemo:
    """Memoization approach"""

    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(col: int, prev: int) -> int:
            """Max columns we can keep from col onwards, with prev as last kept."""
            if col == m:
                return 0

            # Skip this column
            result = dp(col + 1, prev)

            # Keep this column if valid
            if prev == -1 or all(strs[k][prev] <= strs[k][col] for k in range(n)):
                result = max(result, 1 + dp(col + 1, col))

            return result

        return m - dp(0, -1)
