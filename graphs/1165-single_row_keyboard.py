#1165. Single-Row Keyboard
#Easy
#
#There is a special keyboard with all keys in a single row.
#
#Given a string keyboard of length 26 indicating the layout of the keyboard
#(indexed from 0 to 25), initially your finger is at index 0. To type a
#character, you have to move your finger to the index of the desired character.
#The time taken to move your finger from index i to index j is |i - j|.
#
#You want to type a string word. Write a function to calculate how much time
#it takes to type it with one finger.
#
#Example 1:
#Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
#Output: 4
#Explanation: The index moves from 0 to 2 to type 'c' then to 1 to type 'b'
#then to 0 to type 'a'.
#Total time = 2 + 1 + 1 = 4.
#
#Example 2:
#Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
#Output: 73
#
#Constraints:
#    keyboard.length == 26
#    keyboard contains each English lowercase letter exactly once in some order.
#    1 <= word.length <= 10^4
#    word[i] is an English lowercase letter.

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """Map each char to its position, then sum distances"""
        # Build position map
        pos = {c: i for i, c in enumerate(keyboard)}

        total = 0
        current = 0  # Start at index 0

        for c in word:
            total += abs(pos[c] - current)
            current = pos[c]

        return total


class SolutionArray:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """Using array for position lookup"""
        pos = [0] * 26
        for i, c in enumerate(keyboard):
            pos[ord(c) - ord('a')] = i

        total = 0
        current = 0

        for c in word:
            idx = pos[ord(c) - ord('a')]
            total += abs(idx - current)
            current = idx

        return total
