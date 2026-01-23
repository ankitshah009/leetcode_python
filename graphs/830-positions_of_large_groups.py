#830. Positions of Large Groups
#Easy
#
#In a string s of lowercase letters, these letters form consecutive groups of
#the same character.
#
#For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
#"z", and "yy".
#
#A group is identified by an interval [start, end], where start and end denote
#the start and end indices (inclusive) of the group. In the above example,
#"xxxx" has the interval [3, 6].
#
#A group is considered large if it has 3 or more characters.
#
#Return the intervals of every large group sorted in increasing order by start index.
#
#Example 1:
#Input: s = "abbxxxxzzy"
#Output: [[3,6]]
#
#Example 2:
#Input: s = "abc"
#Output: []
#
#Example 3:
#Input: s = "abcdddeeeeaabbbcd"
#Output: [[3,5],[6,9],[12,14]]
#
#Constraints:
#    1 <= s.length <= 1000
#    s contains lowercase English letters only.

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        """
        Track start of each group and count length.
        """
        result = []
        start = 0

        for i in range(len(s)):
            # Check if group ends
            if i == len(s) - 1 or s[i] != s[i + 1]:
                if i - start + 1 >= 3:
                    result.append([start, i])
                start = i + 1

        return result


class SolutionTwoPointer:
    """Explicit two pointer"""

    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1

            if j - i >= 3:
                result.append([i, j - 1])

            i = j

        return result


class SolutionGroupBy:
    """Using itertools.groupby"""

    def largeGroupPositions(self, s: str) -> list[list[int]]:
        from itertools import groupby

        result = []
        i = 0

        for _, group in groupby(s):
            length = len(list(group))
            if length >= 3:
                result.append([i, i + length - 1])
            i += length

        return result
