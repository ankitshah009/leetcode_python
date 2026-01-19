#290. Word Pattern
#Easy
#
#Given a pattern and a string s, find if s follows the same pattern.
#
#Here follow means a full match, such that there is a bijection between a letter
#in pattern and a non-empty word in s.
#
#Example 1:
#Input: pattern = "abba", s = "dog cat cat dog"
#Output: true
#
#Example 2:
#Input: pattern = "abba", s = "dog cat cat fish"
#Output: false
#
#Example 3:
#Input: pattern = "aaaa", s = "dog cat cat dog"
#Output: false
#
#Constraints:
#    1 <= pattern.length <= 300
#    pattern contains only lower-case English letters.
#    1 <= s.length <= 3000
#    s contains only lowercase English letters and spaces ' '.
#    s does not contain any leading or trailing spaces.
#    All the words in s are separated by a single space.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True

    # Alternative using zip and sets
    def wordPatternAlt(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        # Check bijection by comparing number of unique mappings
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
