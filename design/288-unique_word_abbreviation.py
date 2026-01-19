#288. Unique Word Abbreviation
#Medium
#
#The abbreviation of a word is a concatenation of its first letter, the number of
#characters between the first and last letter, and its last letter. If a word has
#only two characters, then it is an abbreviation of itself.
#
#For example:
#    dog --> d1g because there is one letter between the first letter 'd' and the
#    last letter 'g'.
#    internationalization --> i18n because there are 18 letters between the first
#    letter 'i' and the last letter 'n'.
#    it --> it because any word with only two characters is an abbreviation of itself.
#
#Implement the ValidWordAbbr class:
#    ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary
#    of words.
#    boolean isUnique(String word) Returns true if either of the following
#    conditions are met (otherwise returns false):
#        There is no word in dictionary whose abbreviation is equal to word's
#        abbreviation.
#        For any word in dictionary whose abbreviation is equal to word's
#        abbreviation, that word and word are the same.
#
#Example 1:
#Input
#["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
#[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
#Output
#[null, false, true, false, true, true]
#
#Explanation
#ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
#validWordAbbr.isUnique("dear"); // return false, "deer" and "dear" have same abbr
#validWordAbbr.isUnique("cart"); // return true, no word has "c2t" abbr
#validWordAbbr.isUnique("cane"); // return false, "cake" has same "c2e" abbr
#validWordAbbr.isUnique("make"); // return true, no word has "m2e" abbr
#validWordAbbr.isUnique("cake"); // return true, "cake" is in dictionary
#
#Constraints:
#    1 <= dictionary.length <= 3 * 10^4
#    1 <= dictionary[i].length <= 20
#    dictionary[i] consists of lowercase English letters.
#    1 <= word.length <= 20
#    word consists of lowercase English letters.
#    At most 5000 calls will be made to isUnique.

from collections import defaultdict

class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbr_to_words = defaultdict(set)

        for word in dictionary:
            abbr = self._get_abbr(word)
            self.abbr_to_words[abbr].add(word)

    def _get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbr(word)

        # Unique if:
        # 1. No word in dictionary has this abbreviation, OR
        # 2. The only word(s) with this abbreviation is the word itself
        words_with_abbr = self.abbr_to_words[abbr]

        if not words_with_abbr:
            return True

        # Check if all words with same abbr are the same as input word
        return words_with_abbr == {word}


class ValidWordAbbrSimple:
    """Alternative implementation"""

    def __init__(self, dictionary: List[str]):
        self.dict_set = set(dictionary)
        self.abbr_map = {}

        for word in dictionary:
            abbr = self._get_abbr(word)
            if abbr in self.abbr_map:
                # Mark as having multiple words if different
                if self.abbr_map[abbr] != word:
                    self.abbr_map[abbr] = None  # Multiple different words
            else:
                self.abbr_map[abbr] = word

    def _get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbr(word)

        if abbr not in self.abbr_map:
            return True

        # If abbr maps to None, multiple different words have same abbr
        if self.abbr_map[abbr] is None:
            return False

        # Unique if the only word with this abbr is the word itself
        return self.abbr_map[abbr] == word
