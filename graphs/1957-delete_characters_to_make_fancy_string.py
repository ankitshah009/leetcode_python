#1957. Delete Characters to Make Fancy String
#Easy
#
#A fancy string is a string where no three consecutive characters are equal.
#
#Given a string s, delete the minimum possible number of characters from s to
#make it fancy.
#
#Return the final string after the deletion. It can be shown that the answer
#will always be unique.
#
#Example 1:
#Input: s = "leeetcode"
#Output: "leetcode"
#Explanation: Remove an 'e' from the first group of 'e's to create "leetcode".
#
#Example 2:
#Input: s = "aaabaaaa"
#Output: "aabaa"
#
#Example 3:
#Input: s = "aab"
#Output: "aab"
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists only of lowercase English letters.

class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Build result, only add if not creating triple consecutive.
        """
        result = []

        for c in s:
            if len(result) >= 2 and result[-1] == c and result[-2] == c:
                continue
            result.append(c)

        return ''.join(result)


class SolutionGroupBy:
    def makeFancyString(self, s: str) -> str:
        """
        Group consecutive characters, limit each group to 2.
        """
        from itertools import groupby

        result = []

        for char, group in groupby(s):
            count = min(2, len(list(group)))
            result.append(char * count)

        return ''.join(result)


class SolutionCounter:
    def makeFancyString(self, s: str) -> str:
        """
        Track consecutive count.
        """
        if not s:
            return ""

        result = [s[0]]
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            if count < 3:
                result.append(s[i])

        return ''.join(result)
