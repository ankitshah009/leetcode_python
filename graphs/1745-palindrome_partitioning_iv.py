#1745. Palindrome Partitioning IV
#Hard
#
#Given a string s, return true if it is possible to split the string s into
#three non-empty palindromic substrings. Otherwise, return false.
#
#A string is said to be palindrome if it reads the same backward as forward.
#
#Example 1:
#Input: s = "abcbdd"
#Output: true
#
#Example 2:
#Input: s = "bcbddxy"
#Output: false
#
#Constraints:
#    3 <= s.length <= 2000
#    s consists only of lowercase English letters.

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        """
        Precompute palindrome table, then check all split points.
        """
        n = len(s)

        # is_palindrome[i][j] = True if s[i:j+1] is palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        # Base cases
        for i in range(n):
            is_palindrome[i][i] = True

        for i in range(n - 1):
            is_palindrome[i][i + 1] = (s[i] == s[i + 1])

        # Fill for longer substrings
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i + 1][j - 1])

        # Try all split points
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if (is_palindrome[0][i - 1] and
                    is_palindrome[i][j - 1] and
                    is_palindrome[j][n - 1]):
                    return True

        return False


class SolutionOptimized:
    def checkPartitioning(self, s: str) -> bool:
        """
        Optimized with early termination.
        """
        n = len(s)

        # Precompute palindromes using expand around center
        is_palindrome = [[False] * n for _ in range(n)]

        for center in range(n):
            # Odd length
            l, r = center, center
            while l >= 0 and r < n and s[l] == s[r]:
                is_palindrome[l][r] = True
                l -= 1
                r += 1

            # Even length
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                is_palindrome[l][r] = True
                l -= 1
                r += 1

        # Find valid first parts and last parts
        valid_first = set()
        valid_last = set()

        for i in range(n - 2):
            if is_palindrome[0][i]:
                valid_first.add(i + 1)  # First part ends at i, second starts at i+1

        for j in range(2, n):
            if is_palindrome[j][n - 1]:
                valid_last.add(j)  # Last part starts at j

        # Check if middle can be palindrome
        for first_end in valid_first:
            for last_start in valid_last:
                if first_end < last_start:
                    if is_palindrome[first_end][last_start - 1]:
                        return True

        return False


class SolutionManacher:
    def checkPartitioning(self, s: str) -> bool:
        """
        Using Manacher's algorithm for O(n) palindrome preprocessing.
        """
        n = len(s)

        # Build palindrome lookup using DP
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        # Check splits
        for i in range(1, n - 1):
            if dp[0][i - 1]:  # First part is palindrome
                for j in range(i + 1, n):
                    if dp[i][j - 1] and dp[j][n - 1]:  # Middle and last are palindromes
                        return True

        return False
