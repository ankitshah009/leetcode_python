#1422. Maximum Score After Splitting a String
#Easy
#
#Given a string s of zeros and ones, return the maximum score after splitting
#the string into two non-empty substrings (i.e. left substring and right substring).
#
#The score after splitting a string is the number of zeros in the left substring
#plus the number of ones in the right substring.
#
#Example 1:
#Input: s = "011101"
#Output: 5
#Explanation:
#All possible ways of splitting s into two non-empty substrings are:
#left = "0" and right = "1101", score = 1 + 3 = 4
#left = "01" and right = "101", score = 1 + 2 = 3
#left = "011" and right = "101", score = 1 + 2 = 3
#left = "0111" and right = "01", score = 1 + 1 = 2
#left = "01110" and right = "1", score = 2 + 1 = 3
#The maximum score is 5.
#
#Example 2:
#Input: s = "00111"
#Output: 5
#Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
#
#Example 3:
#Input: s = "1111"
#Output: 3
#
#Constraints:
#    2 <= s.length <= 500
#    The string s consists of characters '0' and '1' only.

class Solution:
    def maxScore(self, s: str) -> int:
        """
        Score = zeros_left + ones_right
              = zeros_left + (total_ones - ones_left)
              = zeros_left - ones_left + total_ones

        So maximize zeros_left - ones_left, then add total_ones.
        """
        total_ones = s.count('1')

        max_score = 0
        zeros = 0
        ones = 0

        # Split must leave at least one char on right
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1

            score = zeros + (total_ones - ones)
            max_score = max(max_score, score)

        return max_score


class SolutionBruteForce:
    def maxScore(self, s: str) -> int:
        """O(n^2) brute force"""
        max_score = 0

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)

        return max_score


class SolutionPrefixSum:
    def maxScore(self, s: str) -> int:
        """Using prefix sums"""
        n = len(s)

        # zeros[i] = count of zeros in s[:i]
        # ones[i] = count of ones in s[i:]

        zeros_prefix = [0] * (n + 1)
        for i in range(n):
            zeros_prefix[i + 1] = zeros_prefix[i] + (1 if s[i] == '0' else 0)

        ones_suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            ones_suffix[i] = ones_suffix[i + 1] + (1 if s[i] == '1' else 0)

        max_score = 0
        for i in range(1, n):  # Split at position i (left is s[:i], right is s[i:])
            score = zeros_prefix[i] + ones_suffix[i]
            max_score = max(max_score, score)

        return max_score
