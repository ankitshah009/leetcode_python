#1181. Before and After Puzzle
#Medium
#
#Given a list of phrases, generate a list of Before and After puzzles.
#
#A phrase is a string that consists of lowercase English letters and spaces only.
#No space appears in the start or the end of a phrase. There are no consecutive
#spaces in a phrase.
#
#Before and After puzzles are phrases that are formed by merging two phrases
#where the last word of the first phrase is the same as the first word of the
#second phrase.
#
#Return the Before and After puzzles that can be formed by every two phrases
#phrases[i] and phrases[j] where i != j. Note that the order of matching two
#phrases matters, we want to consider both orders.
#
#You should return a list of distinct strings sorted lexicographically.
#
#Example 1:
#Input: phrases = ["writing code","code rocks"]
#Output: ["writing code rocks"]
#
#Example 2:
#Input: phrases = ["mission statement",
#                   "a]quick",
#                   "statement of",
#                   "a]mission"]
#Output: ["a]mission statement",
#         "a]mission statement of",
#         "a]quick mission statement",
#         "mission statement of"]
#
#Example 3:
#Input: phrases = ["a","b","a"]
#Output: ["a"]
#
#Constraints:
#    1 <= phrases.length <= 100
#    1 <= phrases[i].length <= 100

from typing import List
from collections import defaultdict

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        """
        Group phrases by first word.
        For each phrase, find all phrases whose first word matches last word.
        """
        # Map first word to list of (index, full phrase)
        first_word_map = defaultdict(list)

        for i, phrase in enumerate(phrases):
            first_word = phrase.split()[0]
            first_word_map[first_word].append((i, phrase))

        result = set()

        for i, phrase in enumerate(phrases):
            words = phrase.split()
            last_word = words[-1]

            # Find all phrases starting with last_word
            for j, other in first_word_map[last_word]:
                if i != j:
                    # Merge: phrase + other (minus first word of other)
                    other_words = other.split()
                    merged = phrase + " " + " ".join(other_words[1:]) if len(other_words) > 1 else phrase
                    result.add(merged)

        return sorted(result)


class SolutionExplicit:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        """More explicit approach"""
        n = len(phrases)
        parsed = []

        for phrase in phrases:
            words = phrase.split()
            parsed.append((words[0], words[-1], phrase))

        result = set()

        for i in range(n):
            for j in range(n):
                if i != j:
                    first_i, last_i, phrase_i = parsed[i]
                    first_j, last_j, phrase_j = parsed[j]

                    # Can merge phrase_i with phrase_j if last_i == first_j
                    if last_i == first_j:
                        # Merge: phrase_i + rest of phrase_j
                        rest = phrase_j[len(first_j):].lstrip()
                        if rest:
                            merged = phrase_i + " " + rest
                        else:
                            merged = phrase_i
                        result.add(merged)

        return sorted(result)
