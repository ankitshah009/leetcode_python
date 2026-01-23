#744. Find Smallest Letter Greater Than Target
#Easy
#
#You are given an array of characters letters that is sorted in non-decreasing
#order, and a character target. There are at least two different characters in
#letters.
#
#Return the smallest character in letters that is lexicographically greater
#than target. If such a character does not exist, return the first character
#in letters.
#
#Example 1:
#Input: letters = ["c","f","j"], target = "a"
#Output: "c"
#Explanation: The smallest character that is lexicographically greater than
#'a' in letters is 'c'.
#
#Example 2:
#Input: letters = ["c","f","j"], target = "c"
#Output: "f"
#
#Example 3:
#Input: letters = ["x","x","y","y"], target = "z"
#Output: "x"
#
#Constraints:
#    2 <= letters.length <= 10^4
#    letters[i] is a lowercase English letter.
#    letters is sorted in non-decreasing order.
#    letters contains at least two different characters.
#    target is a lowercase English letter.

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        Binary search for first letter greater than target.
        """
        left, right = 0, len(letters)

        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left % len(letters)]


class SolutionBisect:
    """Using bisect module"""

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        import bisect
        idx = bisect.bisect_right(letters, target)
        return letters[idx % len(letters)]


class SolutionLinear:
    """Linear scan"""

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


class SolutionSet:
    """Using set for unique letters"""

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        seen = set(letters)

        for i in range(1, 27):
            next_char = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if next_char in seen:
                return next_char

        return letters[0]
