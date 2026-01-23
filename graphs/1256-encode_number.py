#1256. Encode Number
#Medium
#
#Given a non-negative integer num, Return its encoding string.
#
#The encoding is done by converting the integer to a string using a secret function.
#
#Example 1:
#Input: num = 23
#Output: "1000"
#
#Example 2:
#Input: num = 107
#Output: "101100"
#
#The pattern:
#0 -> ""
#1 -> "0"
#2 -> "1"
#3 -> "00"
#4 -> "01"
#5 -> "10"
#6 -> "11"
#7 -> "000"
#...
#
#Pattern: encode(n) = binary(n + 1)[1:]  (remove leading 1)
#
#Constraints:
#    0 <= num <= 10^9

class Solution:
    def encode(self, num: int) -> str:
        """
        Pattern: encode(n) = binary(n + 1) without leading '1'
        """
        if num == 0:
            return ""
        return bin(num + 1)[3:]  # bin() returns '0b1...', skip '0b1'


class SolutionExplicit:
    def encode(self, num: int) -> str:
        """Build the encoding explicitly"""
        # Convert num + 1 to binary and remove first bit
        result = []
        num += 1

        while num > 1:
            result.append(str(num % 2))
            num //= 2

        return ''.join(reversed(result))
