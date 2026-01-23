#1987. Number of Unique Good Subsequences
#Hard
#
#You are given a binary string binary. A subsequence of binary is considered
#good if it is not empty and has no leading zeros (with the exception of "0").
#
#Find the number of unique good subsequences of binary.
#
#For example, if binary = "001", then all the good subsequences are ["0", "0",
#"1"], so the unique good subsequences are "0" and "1". Note that subsequences
#"00", "01", and "001" are not good because they have leading zeros.
#
#Return the number of unique good subsequences of binary modulo 10^9 + 7.
#
#A subsequence is a sequence that can be derived from another sequence by
#deleting some or no elements without changing the order of the remaining
#elements.
#
#Example 1:
#Input: binary = "001"
#Output: 2
#Explanation: The good unique subsequences are "0" and "1".
#
#Example 2:
#Input: binary = "11"
#Output: 2
#Explanation: The good unique subsequences are "1" and "11".
#
#Example 3:
#Input: binary = "101"
#Output: 5
#Explanation: "0", "1", "10", "11", "101" are the good unique subsequences.
#
#Constraints:
#    1 <= binary.length <= 10^5
#    binary consists of only '0's and '1's.

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
        DP tracking subsequences ending in 0 and 1.

        For good subsequences (no leading zeros except "0"):
        - Track subsequences starting with 1 (ends0, ends1)
        - Handle "0" separately

        When we see '0': ends0 = ends0 + ends1 (extend existing seqs)
        When we see '1': ends1 = ends0 + ends1 + 1 (extend or start new)
        """
        MOD = 10**9 + 7

        ends0 = 0  # Unique good subsequences ending in 0
        ends1 = 0  # Unique good subsequences ending in 1
        has_zero = False

        for c in binary:
            if c == '0':
                ends0 = (ends0 + ends1) % MOD
                has_zero = True
            else:  # c == '1'
                ends1 = (ends0 + ends1 + 1) % MOD

        # Total = ends0 + ends1 + (1 if has_zero else 0)
        # The +1 for has_zero handles the "0" subsequence
        return (ends0 + ends1 + (1 if has_zero else 0)) % MOD


class SolutionExplained:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
        Detailed explanation:

        We track:
        - ends0: count of unique good subsequences ending in '0'
        - ends1: count of unique good subsequences ending in '1'

        For each character:
        - If '0': We can extend any existing good subsequence with '0'
                  ends0 = ends0 + ends1 (but this counts "0" alone which we handle separately)
        - If '1': We can start a new subsequence "1" or extend any existing
                  ends1 = ends0 + ends1 + 1

        Key insight: "0" alone is special - we count it separately.
        All other good subsequences must start with "1".
        """
        MOD = 10**9 + 7

        # Subsequences starting with 1, ending with 0 or 1
        dp0, dp1 = 0, 0
        has_zero = '0' in binary

        for c in binary:
            if c == '0':
                # Extend sequences ending in 0 or 1 with this 0
                # Can't start new sequence with 0 (would be leading zero)
                dp0 = (dp0 + dp1) % MOD
            else:
                # Extend existing or start new sequence with 1
                dp1 = (dp0 + dp1 + 1) % MOD

        # Add 1 if "0" is possible (handle edge case of just "0")
        return (dp0 + dp1 + (1 if has_zero else 0)) % MOD
