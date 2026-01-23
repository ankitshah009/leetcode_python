#727. Minimum Window Subsequence
#Hard
#
#Given strings s1 and s2, return the minimum contiguous substring part of s1,
#so that s2 is a subsequence of the part.
#
#If there is no such window in s1 that covers all characters in s2, return the
#empty string "". If there are multiple such minimum-length windows, return the
#one with the left-most starting index.
#
#Example 1:
#Input: s1 = "abcdebdde", s2 = "bde"
#Output: "bcde"
#Explanation: "bcde" is the answer because it occurs before "bdde" which has
#the same length. "deb" is not a smaller window because the elements of s2 in
#the window must occur in order.
#
#Example 2:
#Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
#Output: ""
#
#Constraints:
#    1 <= s1.length <= 2 * 10^4
#    1 <= s2.length <= 100
#    s1 and s2 consist of lowercase English letters.

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        DP: dp[i][j] = starting index of min window in s1[:i] containing s2[:j]
        """
        m, n = len(s1), len(s2)

        # dp[j] = starting index of window ending at current position containing s2[:j]
        # Initialize with -1 (not found)
        dp = [-1] * (n + 1)
        dp[0] = 0  # Empty s2 is always a subsequence

        result = ""
        min_len = float('inf')

        for i in range(m):
            # Traverse s2 in reverse to avoid using updated values
            for j in range(n, 0, -1):
                if s1[i] == s2[j - 1] and dp[j - 1] != -1:
                    dp[j] = dp[j - 1]

            # Check if we found a valid window
            if dp[n] != -1:
                length = i - dp[n] + 1
                if length < min_len:
                    min_len = length
                    result = s1[dp[n]:i + 1]

        return result


class SolutionTwoPointer:
    """Two pointer approach: expand then contract"""

    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        result = ""
        min_len = float('inf')
        i = 0

        while i < m:
            # Forward: find s2 as subsequence
            j = 0
            while i < m and j < n:
                if s1[i] == s2[j]:
                    j += 1
                i += 1

            if j < n:
                break  # s2 not found

            # i is now one past the end of the window
            end = i - 1

            # Backward: minimize window
            j = n - 1
            while j >= 0:
                if s1[end] == s2[j]:
                    j -= 1
                end -= 1
            start = end + 1

            # Update result
            if i - start < min_len:
                min_len = i - start
                result = s1[start:i]

            # Move forward from start + 1
            i = start + 1

        return result


class SolutionDPMatrix:
    """Full DP matrix approach"""

    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)

        # dp[i][j] = starting index of min window ending at s1[i-1] for s2[:j]
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        # Empty s2 starts at current position
        for i in range(m + 1):
            dp[i][0] = i

        result = ""
        min_len = float('inf')

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

            if dp[i][n] != -1:
                length = i - dp[i][n]
                if length < min_len:
                    min_len = length
                    result = s1[dp[i][n]:i]

        return result
