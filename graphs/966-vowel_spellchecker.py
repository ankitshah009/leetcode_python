#966. Vowel Spellchecker
#Medium
#
#Given a wordlist, we want to implement a spellchecker that converts a query
#word into a correct word.
#
#For a given query word:
#- If the query matches a word in the wordlist (case-sensitive), return it.
#- If the query matches a word (case-insensitive), return the first match.
#- If the query matches after replacing vowels with any vowel, return first match.
#- Otherwise, return the empty string.
#
#Example 1:
#Input: wordlist = ["KiTe","kite","hare","Hare"],
#       queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
#Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
#
#Constraints:
#    1 <= wordlist.length, queries.length <= 5000
#    1 <= wordlist[i].length, queries[i].length <= 7
#    wordlist[i] and queries[i] consist only of English letters.

class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        """
        Build lookup tables for exact, case-insensitive, and vowel-replaced matches.
        """
        vowels = set('aeiouAEIOU')

        def devowel(word: str) -> str:
            return ''.join('*' if c in vowels else c.lower() for c in word)

        # Exact match set
        exact = set(wordlist)

        # Case-insensitive: map lowercase -> first match
        case_map = {}
        for word in wordlist:
            lower = word.lower()
            if lower not in case_map:
                case_map[lower] = word

        # Vowel pattern: map devoweled -> first match
        vowel_map = {}
        for word in wordlist:
            pattern = devowel(word)
            if pattern not in vowel_map:
                vowel_map[pattern] = word

        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            elif query.lower() in case_map:
                result.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:
                result.append(vowel_map[devowel(query)])
            else:
                result.append("")

        return result


class SolutionExplicit:
    """More explicit matching"""

    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        vowels = 'aeiou'

        def normalize_vowels(word):
            return ''.join('_' if c.lower() in vowels else c.lower() for c in word)

        exact_set = set(wordlist)
        lower_map = {}
        vowel_map = {}

        for word in wordlist:
            low = word.lower()
            if low not in lower_map:
                lower_map[low] = word

            pattern = normalize_vowels(word)
            if pattern not in vowel_map:
                vowel_map[pattern] = word

        result = []
        for q in queries:
            if q in exact_set:
                result.append(q)
                continue

            low = q.lower()
            if low in lower_map:
                result.append(lower_map[low])
                continue

            pattern = normalize_vowels(q)
            if pattern in vowel_map:
                result.append(vowel_map[pattern])
                continue

            result.append("")

        return result
