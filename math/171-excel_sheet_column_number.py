#171. Excel Sheet Column Number
#Easy
#
#Given a string columnTitle that represents the column title as appears in an
#Excel sheet, return its corresponding column number.
#
#For example:
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28
#    ...
#
#Example 1:
#Input: columnTitle = "A"
#Output: 1
#
#Example 2:
#Input: columnTitle = "AB"
#Output: 28
#
#Example 3:
#Input: columnTitle = "ZY"
#Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result


class SolutionReverse:
    """Process from right to left"""

    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        multiplier = 1

        for char in reversed(columnTitle):
            result += (ord(char) - ord('A') + 1) * multiplier
            multiplier *= 26

        return result


class SolutionReduce:
    """Using reduce"""

    def titleToNumber(self, columnTitle: str) -> int:
        from functools import reduce
        return reduce(lambda acc, c: acc * 26 + ord(c) - ord('A') + 1, columnTitle, 0)
