#1639. Number of Ways to Form a Target String Given a Dictionary
#Hard
#
#You are given a list of strings of the same length words and a string target.
#
#Your task is to form target using the given words under the following rules:
#- target should be formed from left to right.
#- To form the ith character (0-indexed) of target, you can choose the kth
#  character of the jth string in words if target[i] = words[j][k].
#- Once you use the kth character of the jth string of words, you can no longer
#  use the xth character of any string in words where x <= k. In other words,
#  all characters to the left of or at index k become unusable for every string.
#- Repeat the process until you form the string target.
#
#Notice that you can use multiple characters from the same string in words
#provided the conditions above are met.
#
#Return the number of ways to form target from words. Since the answer may be
#too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: words = ["acca","bbbb","caca"], target = "aba"
#Output: 6
#Explanation: There are 6 ways to form target.
#"aba" -> index 0 ("a"cca), index 1 (b"b"bb), index 3 (cac"a")
#...
#
#Example 2:
#Input: words = ["abba","baab"], target = "bab"
#Output: 4
#
#Constraints:
#    1 <= words.length <= 1000
#    1 <= words[i].length <= 1000
#    All strings in words have the same length.
#    1 <= target.length <= 1000
#    words[i] and target contain only lowercase English letters.

from typing import List
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        DP approach: count[k][c] = number of words with character c at position k

        dp[i][k] = number of ways to form target[0:i] using columns 0 to k-1
        """
        MOD = 10**9 + 7
        n_cols = len(words[0])
        n_target = len(target)

        # Precompute character counts at each column
        count = [[0] * 26 for _ in range(n_cols)]
        for word in words:
            for k, c in enumerate(word):
                count[k][ord(c) - ord('a')] += 1

        @lru_cache(maxsize=None)
        def dp(i: int, k: int) -> int:
            # i = index in target, k = current column in words

            if i == n_target:
                return 1  # Successfully formed target

            if k == n_cols:
                return 0  # No more columns, but target not complete

            remaining_target = n_target - i
            remaining_cols = n_cols - k

            if remaining_target > remaining_cols:
                return 0  # Not enough columns left

            # Option 1: Skip column k
            result = dp(i, k + 1)

            # Option 2: Use column k for target[i]
            char_idx = ord(target[i]) - ord('a')
            if count[k][char_idx] > 0:
                result += count[k][char_idx] * dp(i + 1, k + 1)
                result %= MOD

            return result

        return dp(0, 0)


class SolutionIterative:
    def numWays(self, words: List[str], target: str) -> int:
        """
        Iterative DP solution.
        """
        MOD = 10**9 + 7
        n_cols = len(words[0])
        n_target = len(target)

        # Count characters at each position
        count = [[0] * 26 for _ in range(n_cols)]
        for word in words:
            for k, c in enumerate(word):
                count[k][ord(c) - ord('a')] += 1

        # dp[i] = number of ways to form target[0:i]
        dp = [0] * (n_target + 1)
        dp[0] = 1

        for k in range(n_cols):
            # Process in reverse to avoid using same column twice
            for i in range(min(k + 1, n_target), 0, -1):
                char_idx = ord(target[i - 1]) - ord('a')
                dp[i] += dp[i - 1] * count[k][char_idx]
                dp[i] %= MOD

        return dp[n_target]


class SolutionOptimized:
    def numWays(self, words: List[str], target: str) -> int:
        """
        Space-optimized iterative DP.
        """
        MOD = 10**9 + 7
        n_cols = len(words[0])
        n_target = len(target)

        # Count characters at each position
        count = [[0] * 26 for _ in range(n_cols)]
        for word in words:
            for k, c in enumerate(word):
                count[k][ord(c) - ord('a')] += 1

        # dp[i] = ways to form first i characters of target
        dp = [1] + [0] * n_target

        for k in range(n_cols):
            for i in range(min(k + 1, n_target), 0, -1):
                char_count = count[k][ord(target[i - 1]) - ord('a')]
                dp[i] = (dp[i] + dp[i - 1] * char_count) % MOD

        return dp[n_target]
