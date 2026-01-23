#520. Detect Capital
#Easy
#
#We define the usage of capitals in a word to be right when one of the following
#cases holds:
#- All letters in this word are capitals, like "USA".
#- All letters in this word are not capitals, like "leetcode".
#- Only the first letter in this word is capital, like "Google".
#
#Given a string word, return true if the usage of capitals in it is right.
#
#Example 1:
#Input: word = "USA"
#Output: true
#
#Example 2:
#Input: word = "FlaG"
#Output: false
#
#Constraints:
#    1 <= word.length <= 100
#    word consists of lowercase and uppercase English letters.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """Check three valid patterns"""
        return word.isupper() or word.islower() or word.istitle()


class SolutionCount:
    """Count uppercase letters"""

    def detectCapitalUse(self, word: str) -> bool:
        upper_count = sum(1 for c in word if c.isupper())

        # All caps, no caps, or only first letter caps
        return upper_count == len(word) or upper_count == 0 or \
               (upper_count == 1 and word[0].isupper())


class SolutionExplicit:
    """Explicit pattern matching"""

    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True

        # All uppercase
        if word[0].isupper() and word[1].isupper():
            return all(c.isupper() for c in word[2:])

        # All lowercase or title case
        return all(c.islower() for c in word[1:])


class SolutionRegex:
    """Using regex"""

    def detectCapitalUse(self, word: str) -> bool:
        import re
        return bool(re.match(r'^[A-Z]*$|^[a-z]*$|^[A-Z][a-z]*$', word))
