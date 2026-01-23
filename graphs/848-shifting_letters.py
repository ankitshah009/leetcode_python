#848. Shifting Letters
#Medium
#
#You are given a string s of lowercase English letters and an integer array
#shifts of the same length.
#
#Call the shift() of a letter, the next letter in the alphabet, (wrapping
#around so that 'z' becomes 'a').
#
#For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
#Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
#
#Return the final string after all such shifts to s are applied.
#
#Example 1:
#Input: s = "abc", shifts = [3,5,9]
#Output: "rpl"
#Explanation: We start with "abc".
#After shifting the first 1 letters by 3, we have "dbc".
#After shifting the first 2 letters by 5, we have "igc".
#After shifting the first 3 letters by 9, we have "rpl".
#
#Example 2:
#Input: s = "aaa", shifts = [1,2,3]
#Output: "gfd"
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of lowercase English letters.
#    shifts.length == s.length
#    0 <= shifts[i] <= 10^9

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        """
        Total shift for position i = sum(shifts[i:]).
        Use suffix sum for O(n) solution.
        """
        n = len(s)
        total_shift = 0
        result = list(s)

        # Process from right to left
        for i in range(n - 1, -1, -1):
            total_shift += shifts[i]
            new_char = (ord(s[i]) - ord('a') + total_shift) % 26
            result[i] = chr(new_char + ord('a'))

        return ''.join(result)


class SolutionSuffixSum:
    """Explicit suffix sum"""

    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(shifts)

        # Compute suffix sums
        suffix_sum = [0] * n
        suffix_sum[-1] = shifts[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + shifts[i]

        result = []
        for i, c in enumerate(s):
            new_idx = (ord(c) - ord('a') + suffix_sum[i]) % 26
            result.append(chr(new_idx + ord('a')))

        return ''.join(result)


class SolutionAccumulate:
    """Using itertools.accumulate"""

    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        from itertools import accumulate

        # Reverse suffix sum = reverse of prefix sum of reversed shifts
        suffix_sums = list(accumulate(reversed(shifts)))[::-1]

        result = []
        for c, shift in zip(s, suffix_sums):
            new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
