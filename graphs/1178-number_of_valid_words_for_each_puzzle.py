#1178. Number of Valid Words for Each Puzzle
#Hard
#
#With respect to a given puzzle string, a word is valid if both the following
#conditions are satisfied:
#    word contains the first letter of puzzle.
#    For each letter in word, that letter is in puzzle.
#
#Return an array answer, where answer[i] is the number of words in the given
#word list words that is valid with respect to the puzzle puzzles[i].
#
#Example 1:
#Input: words = ["aaaa","asas","able","ability","actt","actor","access"],
#puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaeli"]
#Output: [1,1,3,2,4,0]
#Explanation:
#1 valid word for "aboveyz" : "aaaa"
#1 valid word for "abrodyz" : "aaaa"
#3 valid words for "abslute" : "aaaa", "asas", "able"
#2 valid words for "absoryz" : "aaaa", "asas"
#4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
#There are no valid words for "gaeli" since none of words contains letter 'g'.
#
#Example 2:
#Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz",
#"aelpsxy","saelpxy","xaelpsy"]
#Output: [0,1,3,2,0]
#
#Constraints:
#    1 <= words.length <= 10^5
#    4 <= words[i].length <= 50
#    1 <= puzzles.length <= 10^4
#    puzzles[i].length == 7
#    words[i] and puzzles[i] consist of lowercase English letters.
#    Each puzzles[i] does not contain repeated characters.

from typing import List
from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        Convert each word to bitmask of its letters.
        For each puzzle, enumerate all subsets containing first letter.
        Count how many word masks match.
        """
        # Convert words to bitmasks and count
        word_masks = Counter()
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            # Only count if word has <= 7 unique letters (puzzle constraint)
            if bin(mask).count('1') <= 7:
                word_masks[mask] += 1

        result = []

        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))

            # Build puzzle mask
            puzzle_mask = 0
            for c in puzzle:
                puzzle_mask |= 1 << (ord(c) - ord('a'))

            # Enumerate all subsets that include first letter
            count = 0

            # Start with puzzle_mask minus first letter
            subset = puzzle_mask ^ first

            while subset > 0:
                # Add back first letter
                mask = subset | first
                count += word_masks.get(mask, 0)
                # Move to next subset
                subset = (subset - 1) & (puzzle_mask ^ first)

            # Don't forget the subset with only first letter
            count += word_masks.get(first, 0)

            result.append(count)

        return result


class SolutionTrie:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """Trie-based solution"""
        # Build trie of sorted unique characters of each word
        trie = {}

        for word in words:
            # Get sorted unique chars
            chars = sorted(set(word))
            if len(chars) > 7:
                continue

            node = trie
            for c in chars:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = node.get('#', 0) + 1

        result = []

        for puzzle in puzzles:
            first = puzzle[0]
            sorted_puzzle = sorted(puzzle)

            # DFS in trie, must include first letter
            def dfs(node, idx, has_first):
                count = 0

                if '#' in node and has_first:
                    count += node['#']

                for i in range(idx, len(sorted_puzzle)):
                    c = sorted_puzzle[i]
                    if c in node:
                        count += dfs(node[c], i + 1, has_first or (c == first))

                return count

            result.append(dfs(trie, 0, False))

        return result
