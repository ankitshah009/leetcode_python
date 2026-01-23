#880. Decoded String at Index
#Medium
#
#You are given an encoded string s. To decode the string to a tape, the encoded
#string is read one character at a time and the following steps are taken:
#- If the character read is a letter, that letter is written onto the tape.
#- If the character read is a digit (say d), the entire current tape is
#  repeatedly written d - 1 more times in total.
#
#Given an integer k, return the kth letter (1-indexed) in the decoded string.
#
#Example 1:
#Input: s = "leet2code3", k = 10
#Output: "o"
#Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
#
#Example 2:
#Input: s = "ha22", k = 5
#Output: "h"
#Explanation: The decoded string is "hahahaha". The 5th letter is "h".
#
#Example 3:
#Input: s = "a2345678999999999999999", k = 1
#Output: "a"
#
#Constraints:
#    2 <= s.length <= 100
#    s consists of lowercase English letters and digits 2 through 9.
#    s starts with a letter.
#    1 <= k <= 10^9
#    It is guaranteed that k is less than or equal to the length of the decoded string.

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        Work backwards: compute total length, then trace back.
        """
        # Compute total length
        length = 0
        for c in s:
            if c.isdigit():
                length *= int(c)
            else:
                length += 1

        # Work backwards
        for c in reversed(s):
            k %= length

            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                length //= int(c)
            else:
                length -= 1

        return ""


class SolutionExplained:
    """With detailed explanation"""

    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        Key insight: we don't need to build the string.
        - Compute total length
        - Work backwards through s
        - When we see a digit d, length becomes length/d
        - When we see a letter, length becomes length-1
        - k becomes k % length (position in repeated segment)
        - If k == 0 and we're at a letter, that's our answer
        """
        # Forward pass: compute lengths
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        # Backward pass: find kth character
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            k %= size

            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                size //= int(c)
            else:
                size -= 1

        return ""


class SolutionIterative:
    """Alternative iterative approach"""

    def decodeAtIndex(self, s: str, k: int) -> str:
        # Build array of cumulative lengths
        lengths = [0]

        for c in s:
            if c.isdigit():
                lengths.append(lengths[-1] * int(c))
            else:
                lengths.append(lengths[-1] + 1)

        # Binary search for position
        for i in range(len(s) - 1, -1, -1):
            k %= lengths[i + 1]

            if k == 0 and s[i].isalpha():
                return s[i]

        return ""
