#383. Ransom Note
#Easy
#
#Given two strings ransomNote and magazine, return true if ransomNote can be
#constructed by using the letters from magazine and false otherwise.
#
#Each letter in magazine can only be used once in ransomNote.
#
#Example 1:
#Input: ransomNote = "a", magazine = "b"
#Output: false
#
#Example 2:
#Input: ransomNote = "aa", magazine = "ab"
#Output: false
#
#Example 3:
#Input: ransomNote = "aa", magazine = "aab"
#Output: true
#
#Constraints:
#    1 <= ransomNote.length, magazine.length <= 10^5
#    ransomNote and magazine consist of lowercase English letters.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Using Counter"""
        magazine_count = Counter(magazine)

        for char in ransomNote:
            if magazine_count[char] <= 0:
                return False
            magazine_count[char] -= 1

        return True


class SolutionCounterSubtract:
    """Using Counter subtraction"""

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Check if magazine has all required letters
        return not (ransom_count - magazine_count)


class SolutionArray:
    """Using array for lowercase letters"""

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            idx = ord(c) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True


class SolutionCompare:
    """Comparing counters directly"""

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False

        return True
