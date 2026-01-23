#1392. Longest Happy Prefix
#Hard
#
#A string is called a happy prefix if is a non-empty prefix which is also a
#suffix (excluding itself).
#
#Given a string s, return the longest happy prefix of s. Return an empty string
#"" if no such prefix exists.
#
#Example 1:
#Input: s = "level"
#Output: "l"
#Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
#and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix
#is given by "l".
#
#Example 2:
#Input: s = "ababab"
#Output: "abab"
#Explanation: "abab" is the largest prefix which is also suffix. They can overlap
#in the original string.
#
#Example 3:
#Input: s = "leetcodeleet"
#Output: "leet"
#
#Constraints:
#    1 <= s.length <= 10^5
#    s contains only lowercase English letters.

class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Use KMP failure function (LPS array).
        lps[i] = length of longest proper prefix of s[0:i+1] that is also a suffix.
        Answer is lps[n-1].
        """
        n = len(s)
        lps = [0] * n

        # Build LPS array
        length = 0  # Length of previous longest prefix suffix
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return s[:lps[n - 1]]


class SolutionRollingHash:
    def longestPrefix(self, s: str) -> str:
        """
        Rolling hash (Rabin-Karp style).
        Compute hash of prefix and suffix simultaneously.
        """
        n = len(s)
        MOD = 10**9 + 7
        BASE = 31

        prefix_hash = 0
        suffix_hash = 0
        power = 1
        result = 0

        for i in range(n - 1):
            # Add s[i] to prefix hash
            prefix_hash = (prefix_hash * BASE + ord(s[i]) - ord('a') + 1) % MOD

            # Add s[n-1-i] to suffix hash (from the end)
            suffix_hash = (suffix_hash + (ord(s[n - 1 - i]) - ord('a') + 1) * power) % MOD
            power = (power * BASE) % MOD

            if prefix_hash == suffix_hash:
                # Verify (for collision handling)
                if s[:i + 1] == s[n - 1 - i:]:
                    result = i + 1

        return s[:result]


class SolutionZ:
    def longestPrefix(self, s: str) -> str:
        """
        Z-function approach.
        z[i] = length of longest string starting from s[i] that matches prefix.
        Check if z[i] + i == n for any i > 0.
        """
        n = len(s)
        z = [0] * n
        z[0] = n

        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]

        # Find longest where z[i] + i == n
        result = 0
        for i in range(1, n):
            if z[i] + i == n:
                result = max(result, z[i])

        return s[:result]
