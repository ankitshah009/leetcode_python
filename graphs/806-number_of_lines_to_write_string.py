#806. Number of Lines To Write String
#Easy
#
#You are given a string s of lowercase English letters and an array widths
#denoting how many pixels wide each lowercase English letter is. Specifically,
#widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.
#
#You are trying to write s across several lines, where each line is no more
#than 100 pixels wide. Starting at the beginning of s, write as many letters
#as possible on the first line such that the total width does not exceed 100
#pixels. Then, from where you stopped in s, continue writing as many letters
#as possible on the second line. Continue this until you have written all of s.
#
#Return an array result of length 2 where:
#- result[0] is the total number of lines.
#- result[1] is the width of the last line in pixels.
#
#Example 1:
#Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
#Output: [3,60]
#Explanation: All letters have width 10. We can write:
#"abcdefghij" on line 1 (100 pixels)
#"klmnopqrst" on line 2 (100 pixels)
#"uvwxyz" on line 3 (60 pixels)
#
#Example 2:
#Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
#Output: [2,4]
#
#Constraints:
#    widths.length == 26
#    2 <= widths[i] <= 10
#    1 <= s.length <= 1000
#    s contains only lowercase English letters.

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        """
        Greedily fit characters on each line.
        """
        lines = 1
        current_width = 0

        for c in s:
            char_width = widths[ord(c) - ord('a')]
            if current_width + char_width > 100:
                lines += 1
                current_width = char_width
            else:
                current_width += char_width

        return [lines, current_width]


class SolutionReduce:
    """Using reduce"""

    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        from functools import reduce

        def add_char(state, c):
            lines, width = state
            char_width = widths[ord(c) - ord('a')]
            if width + char_width > 100:
                return (lines + 1, char_width)
            return (lines, width + char_width)

        return list(reduce(add_char, s, (1, 0)))
