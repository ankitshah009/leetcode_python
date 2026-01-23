#1974. Minimum Time to Type Word Using Special Typewriter
#Easy
#
#There is a special typewriter with lowercase English letters 'a' to 'z'
#arranged in a circle with a pointer. A character can only be typed if the
#pointer is pointing to that character. The pointer is initially pointing to
#the character 'a'.
#
#Each second, you may perform one of the following operations:
#- Move the pointer one character counterclockwise or clockwise.
#- Type the character the pointer is currently on.
#
#Given a string word, return the minimum number of seconds to type out the
#characters in word.
#
#Example 1:
#Input: word = "abc"
#Output: 5
#Explanation: Move to 'b' (1s), type 'b' (1s), move to 'c' (1s), type 'c' (1s).
#Plus initial type 'a' (1s). Total = 5s.
#
#Example 2:
#Input: word = "bza"
#Output: 7
#
#Example 3:
#Input: word = "zjpc"
#Output: 34
#
#Constraints:
#    1 <= word.length <= 100
#    word consists of lowercase English letters.

class Solution:
    def minTimeToType(self, word: str) -> int:
        """
        Calculate minimum moves between consecutive characters.
        """
        total = 0
        current = 'a'

        for c in word:
            # Distance between current and target
            diff = abs(ord(c) - ord(current))
            # Minimum of clockwise or counterclockwise
            moves = min(diff, 26 - diff)
            # Add moves plus 1 second to type
            total += moves + 1
            current = c

        return total


class SolutionExplicit:
    def minTimeToType(self, word: str) -> int:
        """
        More explicit calculation.
        """
        def min_distance(a: str, b: str) -> int:
            """Minimum circular distance between two characters."""
            diff = abs(ord(a) - ord(b))
            return min(diff, 26 - diff)

        total = 0
        pos = 'a'

        for char in word:
            total += min_distance(pos, char)  # Time to move
            total += 1                         # Time to type
            pos = char

        return total


class SolutionNumeric:
    def minTimeToType(self, word: str) -> int:
        """
        Using numeric positions.
        """
        total = 0
        pos = 0  # 'a' = 0

        for c in word:
            target = ord(c) - ord('a')
            diff = abs(target - pos)
            total += min(diff, 26 - diff) + 1
            pos = target

        return total
