#1573. Number of Ways to Split a String
#Medium
#
#Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3
#where s1 + s2 + s3 = s.
#
#Return the number of ways s can be split such that the number of ones is the
#same in s1, s2, and s3. Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: s = "10101"
#Output: 4
#Explanation: There are four ways to split s in 3 parts where each part contain
#the same number of ones:
#"1|010|1", "1|01|01", "10|10|1", "10|1|01"
#
#Example 2:
#Input: s = "1001"
#Output: 0
#
#Example 3:
#Input: s = "0000"
#Output: 3
#Explanation: There are three ways to split s in 3 parts:
#"0|0|00", "0|00|0", "00|0|0"
#
#Constraints:
#    3 <= s.length <= 10^5
#    s[i] is either '0' or '1'.

class Solution:
    def numWays(self, s: str) -> int:
        """
        Count ones. If not divisible by 3, return 0.
        If all zeros, return C(n-1, 2) = (n-1)*(n-2)/2.
        Otherwise, find positions where we can split.
        """
        MOD = 10**9 + 7
        n = len(s)

        # Count total ones
        total_ones = s.count('1')

        # Must be divisible by 3
        if total_ones % 3 != 0:
            return 0

        # Special case: no ones
        if total_ones == 0:
            # Choose 2 positions from n-1 gaps
            return ((n - 1) * (n - 2) // 2) % MOD

        ones_per_part = total_ones // 3

        # Find the gap between first and second part
        # and between second and third part
        count = 0
        first_cut_ways = 0
        second_cut_ways = 0

        for c in s:
            if c == '1':
                count += 1

            if count == ones_per_part:
                first_cut_ways += 1
            elif count == 2 * ones_per_part:
                second_cut_ways += 1

        return (first_cut_ways * second_cut_ways) % MOD


class SolutionIndices:
    def numWays(self, s: str) -> int:
        """
        Find indices of ones and calculate gaps.
        """
        MOD = 10**9 + 7
        n = len(s)

        # Get indices of all ones
        ones = [i for i, c in enumerate(s) if c == '1']
        total = len(ones)

        if total % 3 != 0:
            return 0

        if total == 0:
            return ((n - 1) * (n - 2) // 2) % MOD

        k = total // 3

        # Gap between end of first part and start of second part
        # First part ends after k ones (index ones[k-1])
        # Second part starts at ones[k]
        first_gap = ones[k] - ones[k - 1]

        # Gap between end of second part and start of third part
        # Second part ends after 2k ones (index ones[2k-1])
        # Third part starts at ones[2k]
        second_gap = ones[2 * k] - ones[2 * k - 1]

        return (first_gap * second_gap) % MOD


class SolutionDetailed:
    def numWays(self, s: str) -> int:
        """
        Detailed explanation with comments.
        """
        MOD = 10**9 + 7
        n = len(s)
        ones = s.count('1')

        # Can't divide into 3 equal parts
        if ones % 3 != 0:
            return 0

        # All zeros: pick 2 cut positions from n-1 gaps
        if ones == 0:
            # C(n-1, 2) ways
            return ((n - 1) * (n - 2) // 2) % MOD

        target = ones // 3

        # Find boundaries
        # After target ones: first cut can be anywhere until next one
        # After 2*target ones: second cut can be anywhere until next one
        count = 0
        first_cut_start = first_cut_end = -1
        second_cut_start = second_cut_end = -1

        for i, c in enumerate(s):
            if c == '1':
                count += 1
                if count == target:
                    first_cut_start = i
                elif count == target + 1:
                    first_cut_end = i
                elif count == 2 * target:
                    second_cut_start = i
                elif count == 2 * target + 1:
                    second_cut_end = i

        # Number of positions for each cut
        ways1 = first_cut_end - first_cut_start
        ways2 = second_cut_end - second_cut_start

        return (ways1 * ways2) % MOD
