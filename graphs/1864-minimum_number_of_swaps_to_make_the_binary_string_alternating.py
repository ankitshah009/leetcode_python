#1864. Minimum Number of Swaps to Make the Binary String Alternating
#Medium
#
#Given a binary string s, return the minimum number of character swaps to make
#it alternating, or -1 if it is impossible.
#
#The string is called alternating if no two adjacent characters are equal. For
#example, the strings "010" and "1010" are alternating, while the string "0100"
#is not.
#
#Any two characters may be swapped, even if they are not adjacent.
#
#Example 1:
#Input: s = "111000"
#Output: 1
#
#Example 2:
#Input: s = "010"
#Output: 0
#
#Example 3:
#Input: s = "1110"
#Output: -1
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] is either '0' or '1'.

class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Count mismatches for both patterns and take minimum.
        """
        ones = s.count('1')
        zeros = len(s) - ones
        n = len(s)

        # Check if alternating is possible
        if abs(ones - zeros) > 1:
            return -1

        def count_mismatches(start_with_one: bool) -> int:
            """Count positions that don't match expected pattern."""
            mismatches = 0
            for i, c in enumerate(s):
                expected = '1' if (i % 2 == 0) == start_with_one else '0'
                if c != expected:
                    mismatches += 1
            return mismatches // 2  # Each swap fixes 2 mismatches

        # Pattern starting with '1': 1010...
        # Pattern starting with '0': 0101...
        if ones > zeros:
            # Must start with '1'
            return count_mismatches(True)
        elif zeros > ones:
            # Must start with '0'
            return count_mismatches(False)
        else:
            # Either pattern works, take minimum
            return min(count_mismatches(True), count_mismatches(False))


class SolutionExplicit:
    def minSwaps(self, s: str) -> int:
        """
        Explicit counting of wrong positions.
        """
        n = len(s)
        ones = s.count('1')
        zeros = n - ones

        if abs(ones - zeros) > 1:
            return -1

        def swaps_for_pattern(first: str) -> int:
            """Count swaps needed if pattern starts with 'first'."""
            wrong_zeros = 0  # 0s at positions that should be 1
            wrong_ones = 0   # 1s at positions that should be 0

            for i, c in enumerate(s):
                expected = first if i % 2 == 0 else ('1' if first == '0' else '0')
                if c != expected:
                    if c == '0':
                        wrong_zeros += 1
                    else:
                        wrong_ones += 1

            if wrong_zeros != wrong_ones:
                return float('inf')
            return wrong_zeros

        if ones > zeros:
            return swaps_for_pattern('1')
        elif zeros > ones:
            return swaps_for_pattern('0')
        else:
            return min(swaps_for_pattern('0'), swaps_for_pattern('1'))
