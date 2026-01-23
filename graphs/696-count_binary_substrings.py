#696. Count Binary Substrings
#Easy
#
#Given a binary string s, return the number of non-empty substrings that have
#the same number of 0's and 1's, and all the 0's and all the 1's in these
#substrings are grouped consecutively.
#
#Substrings that occur multiple times are counted the number of times they
#occur.
#
#Example 1:
#Input: s = "00110011"
#Output: 6
#Explanation: There are 6 substrings that have equal number of consecutive 1's
#and 0's: "0011", "01", "1100", "10", "0011", and "01".
#Notice that some of these substrings repeat and are counted the number of
#times they occur.
#Also, "00110011" is not a valid substring because all the 0's (and 1's) are
#not grouped together.
#
#Example 2:
#Input: s = "10101"
#Output: 4
#Explanation: There are 4 substrings: "10", "01", "10", "01".
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either '0' or '1'.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Count consecutive groups, then add min of adjacent groups.
        e.g., "00110" -> groups [2, 2, 1] -> min(2,2) + min(2,1) = 3
        """
        groups = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i], groups[i - 1])

        return result


class SolutionSpaceOptimized:
    """O(1) space - only track previous group size"""

    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev_count = 0
        curr_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                result += min(prev_count, curr_count)
                prev_count = curr_count
                curr_count = 1

        result += min(prev_count, curr_count)
        return result


class SolutionGroupBy:
    """Using itertools.groupby"""

    def countBinarySubstrings(self, s: str) -> int:
        from itertools import groupby

        groups = [len(list(g)) for _, g in groupby(s)]

        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
