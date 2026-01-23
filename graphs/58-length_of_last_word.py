#58. Length of Last Word
#Easy
#
#Given a string s consisting of words and spaces, return the length of the last
#word in the string.
#
#A word is a maximal substring consisting of non-space characters only.
#
#Example 1:
#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.
#
#Example 2:
#Input: s = "   fly me   to   the moon  "
#Output: 4
#Explanation: The last word is "moon" with length 4.
#
#Example 3:
#Input: s = "luffy is still joyboy"
#Output: 6
#Explanation: The last word is "joyboy" with length 6.
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of only English letters and spaces ' '.
#    There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Traverse from end, skip trailing spaces.
        """
        length = 0
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


class SolutionSplit:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Using split method.
        """
        words = s.split()
        return len(words[-1]) if words else 0


class SolutionStrip:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Strip and find from end.
        """
        s = s.rstrip()
        return len(s) - s.rfind(' ') - 1


class SolutionOneLiner:
    def lengthOfLastWord(self, s: str) -> int:
        """
        One-liner solution.
        """
        return len(s.strip().split()[-1])
