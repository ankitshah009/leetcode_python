#940. Distinct Subsequences II
#Hard
#
#Given a string s, return the number of distinct non-empty subsequences of s.
#Since the answer may be very large, return it modulo 10^9 + 7.
#
#A subsequence of a string is a new string that is formed from the original
#string by deleting some (can be none) of the characters without disturbing
#the relative positions of the remaining characters.
#
#Example 1:
#Input: s = "abc"
#Output: 7
#Explanation: 7 distinct subsequences: "a", "b", "c", "ab", "ac", "bc", "abc".
#
#Example 2:
#Input: s = "aba"
#Output: 6
#Explanation: "a", "b", "ab", "aa", "ba", "aba" (note "a" counted once).
#
#Example 3:
#Input: s = "aaa"
#Output: 3
#
#Constraints:
#    1 <= s.length <= 2000
#    s consists of lowercase English letters.

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        DP: track count of subsequences ending with each character.
        """
        MOD = 10 ** 9 + 7

        # ends[c] = count of distinct subsequences ending with character c
        ends = {}
        total = 0

        for c in s:
            # New subsequences ending with c:
            # - All previous subsequences + c
            # - The single character c itself
            add = total + 1

            # Subtract old subsequences ending with c (to avoid duplicates)
            subtract = ends.get(c, 0)

            # Update
            new_count = (add - subtract) % MOD
            total = (total + new_count) % MOD
            ends[c] = (ends.get(c, 0) + new_count) % MOD

        return total


class SolutionDP:
    """More explicit DP formulation"""

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        # dp[i] = distinct subsequences in s[0:i+1]
        # But we need to track what each char contributes

        # ends[c] = number of distinct subsequences ending with c
        ends = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')

            # New subsequences = all previous + 1 (for single char)
            # But subtract those already ending with c
            prev_total = sum(ends)
            new_ending_c = prev_total + 1

            ends[idx] = new_ending_c % MOD

        return sum(ends) % MOD


class SolutionArray:
    """Using array for last seen position"""

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        # dp[i] = distinct subsequences using s[0:i]
        # ends_with[c] = dp value when c was last added
        dp = 1  # Empty subsequence
        ends_with = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')

            # New dp = 2*dp - ends_with[c]
            # (double: keep or extend each subsequence)
            # (subtract: duplicates from previous occurrence of c)
            new_dp = (2 * dp - ends_with[idx]) % MOD
            ends_with[idx] = dp
            dp = new_dp

        return (dp - 1) % MOD  # Subtract empty subsequence
