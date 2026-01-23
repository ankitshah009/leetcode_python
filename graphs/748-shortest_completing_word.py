#748. Shortest Completing Word
#Easy
#
#Given a string licensePlate and an array of strings words, find the shortest
#completing word in words.
#
#A completing word is a word that contains all the letters in licensePlate.
#Ignore numbers and spaces in licensePlate, and treat letters as case
#insensitive. If a letter appears more than once in licensePlate, then it must
#appear in the word the same number of times or more.
#
#For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b'
#(ignoring case), and 'c' twice. Possible completing words are "abccdef",
#"caaacab", and "cbca".
#
#Return the shortest completing word in words. It is guaranteed an answer
#exists. If there are multiple shortest completing words, return the first
#one that occurs in words.
#
#Example 1:
#Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
#Output: "steps"
#Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
#"step" contains 't' and 'p', but only contains 1 's'.
#"steps" contains 't', 'p', and both 's' characters.
#"stripe" is missing an 's'.
#"stepple" is missing an 's'.
#Since "steps" is the only word containing all the letters, that is the answer.
#
#Example 2:
#Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
#Output: "pest"
#
#Constraints:
#    1 <= licensePlate.length <= 7
#    licensePlate contains digits, letters (uppercase or lowercase), or space.
#    1 <= words.length <= 1000
#    1 <= words[i].length <= 15
#    words[i] consists of lower case English letters.

from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        """
        Count required letters, find shortest word containing all.
        """
        # Extract letters from license plate
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        result = None

        for word in words:
            word_count = Counter(word)

            # Check if word contains all required letters
            if all(word_count[c] >= count for c, count in required.items()):
                if result is None or len(word) < len(result):
                    result = word

        return result


class SolutionSorted:
    """Sort by length and find first matching"""

    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        # Sort by length, keeping original indices for tie-breaking
        indexed_words = [(len(w), i, w) for i, w in enumerate(words)]
        indexed_words.sort()

        for _, _, word in indexed_words:
            word_count = Counter(word)
            if all(word_count[c] >= cnt for c, cnt in required.items()):
                return word

        return ""


class SolutionSubtract:
    """Using Counter subtraction"""

    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        result = None

        for word in words:
            # Check if word contains all required (subtraction gives empty)
            remaining = required - Counter(word)
            if not remaining:
                if result is None or len(word) < len(result):
                    result = word

        return result
