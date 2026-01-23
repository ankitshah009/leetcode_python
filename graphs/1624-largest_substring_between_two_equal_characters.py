#1624. Largest Substring Between Two Equal Characters
#Easy
#
#Given a string s, return the length of the longest substring between two equal
#characters, excluding the two characters. If there is no such substring return -1.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: s = "aa"
#Output: 0
#Explanation: The optimal substring here is an empty string between the two 'a's.
#
#Example 2:
#Input: s = "abca"
#Output: 2
#Explanation: The optimal substring here is "bc".
#
#Example 3:
#Input: s = "cbzxy"
#Output: -1
#Explanation: There are no two equal characters in s.
#
#Constraints:
#    1 <= s.length <= 300
#    s contains only lowercase English letters.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Track first occurrence of each character.
        For each character, distance = current_index - first_index - 1
        """
        first_occurrence = {}
        max_length = -1

        for i, c in enumerate(s):
            if c in first_occurrence:
                max_length = max(max_length, i - first_occurrence[c] - 1)
            else:
                first_occurrence[c] = i

        return max_length


class SolutionTwoPointers:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        For each unique character, find first and last occurrence.
        """
        max_length = -1

        for c in set(s):
            first = s.index(c)
            last = s.rindex(c)
            if first != last:
                max_length = max(max_length, last - first - 1)

        return max_length


class SolutionBruteForce:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Brute force: check all pairs.
        """
        max_length = -1
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    max_length = max(max_length, j - i - 1)

        return max_length


class SolutionArray:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Using array instead of dict for fixed alphabet.
        """
        first = [-1] * 26
        max_len = -1

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            else:
                max_len = max(max_len, i - first[idx] - 1)

        return max_len
