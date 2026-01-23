#824. Goat Latin
#Easy
#
#You are given a string sentence that consist of words separated by spaces.
#Each word consists of lowercase and uppercase letters only.
#
#We would like to convert the sentence to "Goat Latin" using the following rules:
#- If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to
#  the end of the word.
#- If a word begins with a consonant, remove the first letter and append it to
#  the end, then add "ma".
#- Add one letter 'a' to the end of each word per its word index in the
#  sentence, starting with 1.
#
#Return the final sentence.
#
#Example 1:
#Input: sentence = "I speak Goat Latin"
#Output: "Imaa teleska toatGaa atinLaaaa"
#
#Example 2:
#Input: sentence = "The quick brown fox jumped over the lazy dog"
#Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa teleazymaaaaaaaaa ogdmaaaaaaaaaa"
#
#Constraints:
#    1 <= sentence.length <= 150
#    sentence consists of English letters and spaces.
#    sentence has no leading or trailing spaces.
#    All the words in sentence are separated by a single space.

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Apply Goat Latin rules to each word.
        """
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []

        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + 'ma'

            new_word += 'a' * i
            result.append(new_word)

        return ' '.join(result)


class SolutionOneLiner:
    """Compact one-liner"""

    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiouAEIOU'
        return ' '.join(
            (w if w[0] in vowels else w[1:] + w[0]) + 'ma' + 'a' * (i + 1)
            for i, w in enumerate(sentence.split())
        )


class SolutionList:
    """Using list comprehension with explicit logic"""

    def toGoatLatin(self, sentence: str) -> str:
        def convert(word, index):
            vowels = 'aeiouAEIOU'
            if word[0] in vowels:
                return word + 'ma' + 'a' * index
            else:
                return word[1:] + word[0] + 'ma' + 'a' * index

        words = sentence.split()
        return ' '.join(convert(w, i + 1) for i, w in enumerate(words))
