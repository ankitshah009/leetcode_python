#1935. Maximum Number of Words You Can Type
#Easy
#
#There is a malfunctioning keyboard where some letter keys do not work. All
#other keys on the keyboard work properly.
#
#Given a string text of words separated by a single space (no leading or
#trailing spaces) and a string brokenLetters of all distinct letter keys that
#are broken, return the number of words in text you can fully type using this
#keyboard.
#
#Example 1:
#Input: text = "hello world", brokenLetters = "ad"
#Output: 1
#
#Example 2:
#Input: text = "leet code", brokenLetters = "lt"
#Output: 1
#
#Example 3:
#Input: text = "leet code", brokenLetters = "e"
#Output: 0
#
#Constraints:
#    1 <= text.length <= 10^4
#    0 <= brokenLetters.length <= 26
#    text consists of words separated by a single space without any leading or
#    trailing spaces.
#    Each word only consists of lowercase English letters.
#    brokenLetters consists of distinct lowercase English letters.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Count words with no broken letters.
        """
        broken = set(brokenLetters)
        count = 0

        for word in text.split():
            if not any(c in broken for c in word):
                count += 1

        return count


class SolutionSet:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Check set intersection.
        """
        broken = set(brokenLetters)
        return sum(1 for word in text.split() if not set(word) & broken)


class SolutionOneLiner:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        One-liner.
        """
        b = set(brokenLetters)
        return sum(not b & set(w) for w in text.split())
