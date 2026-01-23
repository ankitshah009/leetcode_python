#1358. Number of Substrings Containing All Three Characters
#Medium
#
#Given a string s consisting only of characters a, b and c.
#
#Return the number of substrings containing at least one occurrence of all
#these characters a, b and c.
#
#Example 1:
#Input: s = "abcabc"
#Output: 10
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
#
#Example 2:
#Input: s = "aaacb"
#Output: 3
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
#
#Example 3:
#Input: s = "abc"
#Output: 1
#
#Constraints:
#    3 <= s.length <= 5 * 10^4
#    s only consists of a, b or c characters.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Sliding window: for each right pointer, find the leftmost valid left.
        All substrings from 0 to left-1 as starting points with right as ending are valid.
        """
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            # Shrink window while all three chars are present
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # All substrings starting from [0, left] ending at right are valid
                result += n - right
                count[s[left]] -= 1
                left += 1

        return result


class SolutionLastIndex:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Track last index of each character.
        For each position, valid substrings start from min(last_a, last_b, last_c) + 1.
        """
        last = {'a': -1, 'b': -1, 'c': -1}
        result = 0

        for i, c in enumerate(s):
            last[c] = i

            # Minimum of last indices - all positions before this can be starting points
            min_last = min(last.values())
            result += min_last + 1

        return result


class SolutionSimpler:
    def numberOfSubstrings(self, s: str) -> int:
        """Track last positions with array"""
        last = [-1, -1, -1]  # Last index of a, b, c
        result = 0

        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
            result += 1 + min(last)

        return result
