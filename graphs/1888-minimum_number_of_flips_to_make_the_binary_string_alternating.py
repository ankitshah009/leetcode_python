#1888. Minimum Number of Flips to Make the Binary String Alternating
#Medium
#
#You are given a binary string s. You are allowed to perform two types of
#operations on the string in any sequence:
#
#Type-1: Remove the character at the start of the string s and append it to the
#end of the string.
#Type-2: Pick any character in s and flip its value, i.e., if its value is '0'
#it becomes '1' and vice-versa.
#
#Return the minimum number of type-2 operations you need to perform such that s
#becomes alternating.
#
#The string is called alternating if no two adjacent characters are equal.
#
#Example 1:
#Input: s = "111000"
#Output: 2
#
#Example 2:
#Input: s = "010"
#Output: 0
#
#Example 3:
#Input: s = "1110"
#Output: 1
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either '0' or '1'.

class Solution:
    def minFlips(self, s: str) -> int:
        """
        Sliding window: double the string, slide window of size n.
        """
        n = len(s)
        s = s + s  # Double to simulate all rotations

        # Two target patterns
        alt1 = ''.join('0' if i % 2 == 0 else '1' for i in range(2 * n))
        alt2 = ''.join('1' if i % 2 == 0 else '0' for i in range(2 * n))

        # Count mismatches in first window
        diff1 = sum(1 for i in range(n) if s[i] != alt1[i])
        diff2 = sum(1 for i in range(n) if s[i] != alt2[i])

        min_flips = min(diff1, diff2)

        # Slide window
        for i in range(n, 2 * n):
            # Add new character
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1

            # Remove old character
            if s[i - n] != alt1[i - n]:
                diff1 -= 1
            if s[i - n] != alt2[i - n]:
                diff2 -= 1

            min_flips = min(min_flips, diff1, diff2)

        return min_flips


class SolutionOptimized:
    def minFlips(self, s: str) -> int:
        """
        Optimized: track mismatches for even/odd positions.
        """
        n = len(s)

        # Count mismatches at even and odd positions for pattern starting with '0'
        # Pattern "0101...": mismatches = s[i] != str(i % 2)
        # Pattern "1010...": mismatches = s[i] != str(1 - i % 2)

        def count_mismatches_start0(s):
            return sum(1 for i, c in enumerate(s) if c != str(i % 2))

        def count_mismatches_start1(s):
            return sum(1 for i, c in enumerate(s) if c != str(1 - i % 2))

        # For odd length, only one pattern works per rotation
        # For even length, both patterns give same count after any rotation

        if n % 2 == 0:
            return min(count_mismatches_start0(s), count_mismatches_start1(s))

        # For odd length, use sliding window on doubled string
        doubled = s + s
        diff0 = count_mismatches_start0(s)
        diff1 = count_mismatches_start1(s)

        min_flips = min(diff0, diff1)

        for i in range(n):
            # Character leaving window
            if s[i] != str(i % 2):
                diff0 -= 1
            if s[i] != str(1 - i % 2):
                diff1 -= 1

            # Character entering window (at position i + n in pattern)
            new_idx = i + n
            if doubled[new_idx] != str(new_idx % 2):
                diff0 += 1
            if doubled[new_idx] != str(1 - new_idx % 2):
                diff1 += 1

            min_flips = min(min_flips, diff0, diff1)

        return min_flips
