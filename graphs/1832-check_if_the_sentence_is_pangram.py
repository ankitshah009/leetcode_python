#1832. Check if the Sentence Is Pangram
#Easy
#
#A pangram is a sentence where every letter of the English alphabet appears at
#least once.
#
#Given a string sentence containing only lowercase English letters, return true
#if sentence is a pangram, or false otherwise.
#
#Example 1:
#Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
#Output: true
#
#Example 2:
#Input: sentence = "leetcode"
#Output: false
#
#Constraints:
#    1 <= sentence.length <= 1000
#    sentence consists of lowercase English letters.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Check if all 26 letters are present.
        """
        return len(set(sentence)) == 26


class SolutionBitmask:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Using bitmask to track letters.
        """
        mask = 0
        for c in sentence:
            mask |= 1 << (ord(c) - ord('a'))
        return mask == (1 << 26) - 1


class SolutionSet:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Check if alphabet is subset of sentence.
        """
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        return alphabet.issubset(set(sentence))


class SolutionAll:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Using all() with generator.
        """
        return all(c in sentence for c in 'abcdefghijklmnopqrstuvwxyz')
