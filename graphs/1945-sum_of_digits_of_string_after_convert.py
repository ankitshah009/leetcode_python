#1945. Sum of Digits of String After Convert
#Easy
#
#You are given a string s consisting of lowercase English letters, and an
#integer k.
#
#First, convert s into an integer by replacing each letter with its position in
#the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then,
#transform the integer by replacing it with the sum of its digits. Repeat the
#transform operation k times in total.
#
#For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by
#the following operations:
#- Convert: "zbax" -> "(26)(2)(1)(24)" -> "262124" -> 262124
#- Transform #1: 262124 -> 2 + 6 + 2 + 1 + 2 + 4 -> 17
#- Transform #2: 17 -> 1 + 7 -> 8
#
#Return the resulting integer after performing the operations described above.
#
#Example 1:
#Input: s = "iiii", k = 1
#Output: 36
#
#Example 2:
#Input: s = "leetcode", k = 2
#Output: 6
#
#Example 3:
#Input: s = "zbax", k = 2
#Output: 8
#
#Constraints:
#    1 <= s.length <= 100
#    1 <= k <= 10
#    s consists of lowercase English letters.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        Convert to number string, then sum digits k times.
        """
        # Convert to digits string
        num_str = ''.join(str(ord(c) - ord('a') + 1) for c in s)

        # Sum digits k times
        result = sum(int(d) for d in num_str)

        for _ in range(k - 1):
            result = sum(int(d) for d in str(result))

        return result


class SolutionIterative:
    def getLucky(self, s: str, k: int) -> int:
        """
        Iterative approach.
        """
        # Convert characters to position numbers
        digits = []
        for c in s:
            pos = ord(c) - ord('a') + 1
            digits.extend(int(d) for d in str(pos))

        # Transform k times
        total = sum(digits)

        for _ in range(k - 1):
            total = sum(int(d) for d in str(total))

        return total


class SolutionOneLiner:
    def getLucky(self, s: str, k: int) -> int:
        """
        Compact solution.
        """
        from functools import reduce

        num = ''.join(str(ord(c) - 96) for c in s)
        return reduce(lambda x, _: sum(int(d) for d in str(x)), range(k), sum(int(d) for d in num))
