#1540. Can Convert String in K Moves
#Medium
#
#Given two strings s and t, your goal is to convert s into t in k moves or less.
#
#During the ith (1 <= i <= k) move you can:
#- Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has
#  not been chosen in any previous move, and shift the character at that index i times.
#- Do nothing.
#
#Shifting a character means replacing it by the next letter in the alphabet
#(wrapping around so that 'z' becomes 'a'). Shifting a character by i means
#applying the shift operations i times.
#
#Remember that any index j can be picked at most once.
#
#Return true if it's possible to convert s into t in no more than k moves, otherwise
#return false.
#
#Example 1:
#Input: s = "input", t = "ouput", k = 9
#Output: true
#Explanation: In the 6th move, we shift 'i' 6 times to get 'o'.
#And in the 7th move we shift 'n' 7 times to get 'u'.
#
#Example 2:
#Input: s = "abc", t = "bcd", k = 10
#Output: false
#Explanation: We need to shift each character in s one time to convert it into t.
#We can shift 'a' to 'b' during the 1st move. However, there is no way to shift
#the other characters in the remaining moves to obtain t from s.
#
#Example 3:
#Input: s = "aab", t = "bbb", k = 27
#Output: true
#Explanation: In the 1st move, we shift the first 'a' 1 time to get 'b'.
#In the 27th move, we shift the second 'a' 27 times to get 'b'.
#
#Constraints:
#    1 <= s.length, t.length <= 10^5
#    0 <= k <= 10^9
#    s, t contain only lowercase English letters.

from collections import Counter

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """
        For each position, calculate required shift.
        Same shifts need different moves (1, 27, 53, ... for shift 1).

        Count occurrences of each shift needed.
        For shift x appearing c times, we need moves: x, x+26, x+52, ..., x+26*(c-1)
        The maximum move needed is x + 26*(c-1), which must be <= k.
        """
        if len(s) != len(t):
            return False

        # Count required shifts (1 to 26)
        shift_count = [0] * 26

        for cs, ct in zip(s, t):
            shift = (ord(ct) - ord(cs)) % 26
            if shift > 0:
                shift_count[shift] += 1

        # Check if all shifts can be done within k moves
        for shift in range(1, 26):
            count = shift_count[shift]
            if count > 0:
                # Max move needed for this shift
                max_move = shift + 26 * (count - 1)
                if max_move > k:
                    return False

        return True


class SolutionCounter:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """
        Using Counter for shift counting.
        """
        if len(s) != len(t):
            return False

        shifts = []
        for cs, ct in zip(s, t):
            shift = (ord(ct) - ord(cs)) % 26
            if shift != 0:
                shifts.append(shift)

        shift_counts = Counter(shifts)

        for shift, count in shift_counts.items():
            # Need moves: shift, shift+26, shift+52, ...
            # Last move: shift + 26*(count-1)
            if shift + 26 * (count - 1) > k:
                return False

        return True


class SolutionArray:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """
        Array-based counting with early exit.
        """
        if len(s) != len(t):
            return False

        # needed[i] = number of times we need shift i
        needed = [0] * 26

        for i in range(len(s)):
            shift = (ord(t[i]) - ord(s[i])) % 26
            if shift > 0:
                needed[shift] += 1

        # Check constraints
        for shift in range(1, 26):
            cnt = needed[shift]
            if cnt > 0:
                # Maximum move required
                max_required = shift + 26 * (cnt - 1)
                if max_required > k:
                    return False

        return True


class SolutionMath:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """
        Mathematical formulation.
        """
        if len(s) != len(t):
            return False

        # Count how many of each shift we need
        counts = [0] * 26

        for cs, ct in zip(s, t):
            diff = (ord(ct) - ord(cs)) % 26
            counts[diff] += 1

        # For shift d (1 <= d <= 25) with count c:
        # We use moves d, d+26, d+52, ..., d+26(c-1)
        # The largest is d + 26(c-1), must be <= k

        for d in range(1, 26):
            c = counts[d]
            if c > 0:
                largest_move = d + 26 * (c - 1)
                if largest_move > k:
                    return False

        return True
