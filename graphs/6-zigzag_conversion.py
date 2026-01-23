#6. Zigzag Conversion
#Medium
#
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
#of rows like this:
#
#P   A   H   N
#A P L S I I G
#Y   I   R
#
#And then read line by line: "PAHNAPLSIIGYIR"
#
#Write the code that will take a string and make this conversion given a number
#of rows.
#
#Example 1:
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#
#Example 2:
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#
#Example 3:
#Input: s = "A", numRows = 1
#Output: "A"
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists of English letters (lower-case and upper-case), ',' and '.'.
#    1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Simulate the zigzag pattern using rows array.
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return ''.join(rows)


class SolutionMath:
    def convert(self, s: str, numRows: int) -> str:
        """
        Calculate indices mathematically.
        """
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        cycle_len = 2 * numRows - 2

        for row in range(numRows):
            for j in range(row, len(s), cycle_len):
                result.append(s[j])

                # Middle rows have diagonal character
                if row != 0 and row != numRows - 1:
                    diagonal = j + cycle_len - 2 * row
                    if diagonal < len(s):
                        result.append(s[diagonal])

        return ''.join(result)


class SolutionListComprehension:
    def convert(self, s: str, numRows: int) -> str:
        """
        Using list comprehension.
        """
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        row, step = 0, 1

        for c in s:
            rows[row].append(c)
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(''.join(row) for row in rows)
