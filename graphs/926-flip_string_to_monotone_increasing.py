#926. Flip String to Monotone Increasing
#Medium
#
#A binary string is monotone increasing if it consists of some number of 0's
#(possibly none), followed by some number of 1's (also possibly none).
#
#You are given a binary string s. You can flip s[i] changing it from 0 to 1 or
#from 1 to 0.
#
#Return the minimum number of flips to make s monotone increasing.
#
#Example 1:
#Input: s = "00110"
#Output: 1
#Explanation: Flip the last digit to get 00111.
#
#Example 2:
#Input: s = "010110"
#Output: 2
#Explanation: Flip to get 011111, or 000111.
#
#Example 3:
#Input: s = "00011000"
#Output: 2
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either '0' or '1'.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        For each position, track: flip all 1s before to 0, or flip current 0 to 1.
        """
        ones_before = 0  # Count of 1s we've seen
        flips = 0  # Minimum flips needed

        for c in s:
            if c == '1':
                ones_before += 1
            else:
                # Either flip this 0 to 1, or flip all previous 1s to 0
                flips = min(flips + 1, ones_before)

        return flips


class SolutionDP:
    """Explicit DP"""

    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)

        # dp0[i] = min flips to make s[0:i] end with 0
        # dp1[i] = min flips to make s[0:i] end with 1
        dp0 = 0
        dp1 = 0

        for c in s:
            if c == '0':
                # End with 0: no flip needed, but can't have 1s before
                # End with 1: flip this 0 to 1
                dp0 = dp0
                dp1 = min(dp0, dp1) + 1
            else:
                # End with 0: impossible after seeing 1, or flip this 1 to 0
                # End with 1: no flip needed
                dp0 = dp0 + 1
                dp1 = min(dp0 - 1, dp1)

        return min(dp0, dp1)


class SolutionPrefixSum:
    """Using prefix sum"""

    def minFlipsMonoIncr(self, s: str) -> int:
        # prefix[i] = number of 1s in s[0:i]
        n = len(s)
        prefix_ones = [0] * (n + 1)

        for i, c in enumerate(s):
            prefix_ones[i + 1] = prefix_ones[i] + (1 if c == '1' else 0)

        # Try all split points: all 0s before i, all 1s from i
        result = n
        for i in range(n + 1):
            ones_before = prefix_ones[i]  # Flip these to 0
            zeros_after = (n - i) - (prefix_ones[n] - prefix_ones[i])  # Flip these to 1
            result = min(result, ones_before + zeros_after)

        return result
