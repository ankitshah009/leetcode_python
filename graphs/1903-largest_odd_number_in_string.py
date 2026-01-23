#1903. Largest Odd Number in String
#Easy
#
#You are given a string num, representing a large integer. Return the
#largest-valued odd integer (as a string) that is a non-empty substring of num,
#or an empty string "" if no odd integer exists.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: num = "52"
#Output: "5"
#
#Example 2:
#Input: num = "4206"
#Output: ""
#
#Example 3:
#Input: num = "35427"
#Output: "35427"
#
#Constraints:
#    1 <= num.length <= 10^5
#    num only consists of digits and does not contain any leading zeros.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Find rightmost odd digit, return prefix up to it.
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""


class SolutionOddCheck:
    def largestOddNumber(self, num: str) -> str:
        """
        Check if digit is odd using character.
        """
        for i in range(len(num) - 1, -1, -1):
            if num[i] in '13579':
                return num[:i + 1]
        return ""


class SolutionRstrip:
    def largestOddNumber(self, num: str) -> str:
        """
        Remove trailing even digits.
        """
        return num.rstrip('02468')
