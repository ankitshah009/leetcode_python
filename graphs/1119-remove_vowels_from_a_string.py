#1119. Remove Vowels from a String
#Easy
#
#Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it,
#and return the new string.
#
#Example 1:
#Input: s = "leetcodeisacommunityforcoders"
#Output: "ltcdscmmntyfrcdrs"
#
#Example 2:
#Input: s = "aeiou"
#Output: ""
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists of only lowercase English letters.

class Solution:
    def removeVowels(self, s: str) -> str:
        """Filter out vowels"""
        vowels = set('aeiou')
        return ''.join(c for c in s if c not in vowels)


class SolutionTranslate:
    def removeVowels(self, s: str) -> str:
        """Using str.translate"""
        return s.translate(str.maketrans('', '', 'aeiou'))


class SolutionReplace:
    def removeVowels(self, s: str) -> str:
        """Replace each vowel"""
        for v in 'aeiou':
            s = s.replace(v, '')
        return s


class SolutionRegex:
    def removeVowels(self, s: str) -> str:
        """Using regex"""
        import re
        return re.sub(r'[aeiou]', '', s)
