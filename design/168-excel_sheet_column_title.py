#168. Excel Sheet Column Title
#Easy
#
#Given an integer columnNumber, return its corresponding column title as it
#appears in an Excel sheet.
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
#Input: columnNumber = 1
#Output: "A"
#
#Example 2:
#Input: columnNumber = 28
#Output: "AB"
#
#Example 3:
#Input: columnNumber = 701
#Output: "ZY"

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-indexed
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            columnNumber //= 26

        return ''.join(reversed(result))


class SolutionRecursive:
    """Recursive approach"""

    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""

        columnNumber -= 1
        return self.convertToTitle(columnNumber // 26) + chr(ord('A') + columnNumber % 26)


class SolutionIterative:
    """Alternative iterative with string concatenation"""

    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = chr(ord('A') + columnNumber % 26) + result
            columnNumber //= 26

        return result
