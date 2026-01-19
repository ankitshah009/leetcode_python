#87. Scramble String
#Hard
#
#We can scramble a string s to get a string t using the following algorithm:
#
#If the length of the string is 1, stop.
#If the length of the string is > 1, do the following:
#    Split the string into two non-empty substrings at a random index.
#    Randomly decide to swap the two substrings or keep them in the same order.
#    Apply step 1 recursively on each of the two substrings.
#
#Given two strings s1 and s2 of the same length, return true if s2 is a scrambled
#string of s1, otherwise, return false.
#
#Example 1:
#Input: s1 = "great", s2 = "rgeat"
#Output: true
#
#Example 2:
#Input: s1 = "abcde", s2 = "caebd"
#Output: false
#
#Example 3:
#Input: s1 = "a", s2 = "a"
#Output: true
#
#Constraints:
#    s1.length == s2.length
#    1 <= s1.length <= 30
#    s1 and s2 consist of lowercase English letters.

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dp(i1, i2, length):
            if (i1, i2, length) in memo:
                return memo[(i1, i2, length)]

            # Base case: single character
            if length == 1:
                return s1[i1] == s2[i2]

            # Check if substrings have same characters
            if sorted(s1[i1:i1+length]) != sorted(s2[i2:i2+length]):
                memo[(i1, i2, length)] = False
                return False

            # Try all possible split points
            for k in range(1, length):
                # Case 1: No swap
                if dp(i1, i2, k) and dp(i1 + k, i2 + k, length - k):
                    memo[(i1, i2, length)] = True
                    return True

                # Case 2: Swap
                if dp(i1, i2 + length - k, k) and dp(i1 + k, i2, length - k):
                    memo[(i1, i2, length)] = True
                    return True

            memo[(i1, i2, length)] = False
            return False

        return dp(0, 0, len(s1))
