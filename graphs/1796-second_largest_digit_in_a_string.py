#1796. Second Largest Digit in a String
#Easy
#
#Given an alphanumeric string s, return the second largest numerical digit that
#appears in s, or -1 if it does not exist.
#
#An alphanumeric string is a string consisting of lowercase English letters and
#digits.
#
#Example 1:
#Input: s = "dfa12321afd"
#Output: 2
#
#Example 2:
#Input: s = "abc1111"
#Output: -1
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of only lowercase English letters and/or digits.

class Solution:
    def secondHighest(self, s: str) -> int:
        """
        Track two largest digits.
        """
        first = second = -1

        for c in s:
            if c.isdigit():
                d = int(c)
                if d > first:
                    second = first
                    first = d
                elif d < first and d > second:
                    second = d

        return second


class SolutionSet:
    def secondHighest(self, s: str) -> int:
        """
        Collect unique digits and find second largest.
        """
        digits = {int(c) for c in s if c.isdigit()}

        if len(digits) < 2:
            return -1

        digits.remove(max(digits))
        return max(digits)


class SolutionSorted:
    def secondHighest(self, s: str) -> int:
        """
        Sort unique digits.
        """
        digits = sorted(set(int(c) for c in s if c.isdigit()), reverse=True)
        return digits[1] if len(digits) >= 2 else -1


class SolutionFilter:
    def secondHighest(self, s: str) -> int:
        """
        Using filter and sorted.
        """
        digits = sorted(set(filter(str.isdigit, s)), reverse=True)
        return int(digits[1]) if len(digits) >= 2 else -1
