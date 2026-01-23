#1880. Check if Word Equals Summation of Two Words
#Easy
#
#The letter value of a letter is its position in the alphabet starting from 0
#(i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
#
#The numerical value of some string of lowercase English letters s is the
#concatenation of the letter values of each letter in s, which is then
#converted into an integer.
#
#For example, if s = "acb", we concatenate each letter's letter value,
#resulting in "021". After converting it, we get 21.
#
#You are given three strings firstWord, secondWord, and targetWord, each
#consisting of lowercase English letters 'a' through 'j' inclusive.
#
#Return true if the summation of the numerical values of firstWord and
#secondWord equals the numerical value of targetWord, or false otherwise.
#
#Example 1:
#Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
#Output: true
#
#Example 2:
#Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
#Output: false
#
#Example 3:
#Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
#Output: true
#
#Constraints:
#    1 <= firstWord.length, secondWord.length, targetWord.length <= 8
#    firstWord, secondWord, and targetWord consist of lowercase English letters
#    from 'a' to 'j' inclusive.

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Convert each word to its numerical value and check sum.
        """
        def to_value(word: str) -> int:
            return int(''.join(str(ord(c) - ord('a')) for c in word))

        return to_value(firstWord) + to_value(secondWord) == to_value(targetWord)


class SolutionManual:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Manual conversion without string operations.
        """
        def to_value(word: str) -> int:
            result = 0
            for c in word:
                result = result * 10 + (ord(c) - ord('a'))
            return result

        return to_value(firstWord) + to_value(secondWord) == to_value(targetWord)


class SolutionReduce:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Using functools.reduce.
        """
        from functools import reduce

        def to_value(word: str) -> int:
            return reduce(lambda acc, c: acc * 10 + (ord(c) - ord('a')), word, 0)

        return to_value(firstWord) + to_value(secondWord) == to_value(targetWord)


class SolutionCompact:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        One-liner helper.
        """
        f = lambda w: int(''.join(chr(ord(c) - ord('a') + ord('0')) for c in w))
        return f(firstWord) + f(secondWord) == f(targetWord)
