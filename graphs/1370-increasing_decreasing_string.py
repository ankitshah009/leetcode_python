#1370. Increasing Decreasing String
#Easy
#
#You are given a string s. Reorder the string using the following algorithm:
#    1. Pick the smallest character from s and append it to the result.
#    2. Pick the smallest character from s which is greater than the last
#       appended character to the result and append it.
#    3. Repeat step 2 until you cannot pick more characters.
#    4. Pick the largest character from s and append it to the result.
#    5. Pick the largest character from s which is smaller than the last
#       appended character to the result and append it.
#    6. Repeat step 5 until you cannot pick more characters.
#    7. Repeat the steps from 1 to 6 until you pick all characters from s.
#
#In each step, If the smallest or the largest character appears more than once
#you can choose any occurrence and append it to the result.
#
#Return the result string after sorting s with this algorithm.
#
#Example 1:
#Input: s = "aaaabbbbcccc"
#Output: "abccbaabccba"
#
#Example 2:
#Input: s = "rat"
#Output: "art"
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of only lowercase English letters.

from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        """
        Count characters, then alternately pick ascending and descending.
        """
        count = Counter(s)
        result = []
        n = len(s)

        while len(result) < n:
            # Ascending: pick smallest to largest
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1

            # Descending: pick largest to smallest
            for c in 'zyxwvutsrqponmlkjihgfedcba':
                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1

        return ''.join(result)


class SolutionArray:
    def sortString(self, s: str) -> str:
        """Using array instead of Counter"""
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        n = len(s)

        while len(result) < n:
            # Ascending
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1

            # Descending
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1

        return ''.join(result)
