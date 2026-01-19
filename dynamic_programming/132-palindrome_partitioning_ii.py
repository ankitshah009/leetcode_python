#132. Palindrome Partitioning II
#Hard
#
#Given a string s, partition s such that every substring of the partition is a
#palindrome.
#
#Return the minimum cuts needed for a palindrome partitioning of s.
#
#Example 1:
#Input: s = "aab"
#Output: 1
#Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
#Example 2:
#Input: s = "a"
#Output: 0
#
#Example 3:
#Input: s = "ab"
#Output: 1
#
#Constraints:
#    1 <= s.length <= 2000
#    s consists of lowercase English letters only.

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_palindrome[i][j] = True if s[i:j+1] is palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    is_palindrome[i][j] = (s[i] == s[j])
                else:
                    is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i+1][j-1])

        # dp[i] = minimum cuts for s[0:i+1]
        dp = [float('inf')] * n

        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n-1]

    # Optimized approach with expanding around centers
    def minCutOptimized(self, s: str) -> int:
        n = len(s)
        dp = list(range(n))  # dp[i] = min cuts for s[0:i+1]

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left-1] + 1)
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)      # Odd length palindromes
            expand(i, i + 1)  # Even length palindromes

        return dp[n-1]
