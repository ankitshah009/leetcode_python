#792. Number of Matching Subsequences
#Medium
#
#Given a string s and an array of strings words, return the number of words[i]
#that is a subsequence of s.
#
#A subsequence of a string is a new string generated from the original string
#with some characters (can be none) deleted without changing the relative order
#of the remaining characters.
#
#Example 1:
#Input: s = "abcde", words = ["a","bb","acd","ace"]
#Output: 3
#Explanation: There are three strings in words that are subsequences of s:
#"a", "acd", "ace".
#
#Example 2:
#Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","gy"]
#Output: 2
#
#Constraints:
#    1 <= s.length <= 5 * 10^4
#    1 <= words.length <= 5000
#    1 <= words[i].length <= 50
#    s and words[i] consist of only lowercase English letters.

from collections import defaultdict
from bisect import bisect_left

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        """
        Use binary search with precomputed character positions.
        """
        # Precompute positions of each character
        char_positions = defaultdict(list)
        for i, c in enumerate(s):
            char_positions[c].append(i)

        def is_subsequence(word):
            prev_idx = -1
            for c in word:
                if c not in char_positions:
                    return False
                positions = char_positions[c]
                # Find first position > prev_idx
                idx = bisect_left(positions, prev_idx + 1)
                if idx == len(positions):
                    return False
                prev_idx = positions[idx]
            return True

        return sum(1 for word in words if is_subsequence(word))


class SolutionWaiting:
    """Waiting buckets approach - process s once"""

    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Buckets for words waiting for each character
        waiting = defaultdict(list)

        for word in words:
            waiting[word[0]].append(iter(word[1:]))

        count = 0
        for c in s:
            # Process all words waiting for character c
            current_waiting = waiting[c]
            waiting[c] = []

            for it in current_waiting:
                next_char = next(it, None)
                if next_char is None:
                    count += 1
                else:
                    waiting[next_char].append(it)

        return count


class SolutionTrie:
    """Trie-based approach for duplicate words"""

    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        from collections import Counter

        word_count = Counter(words)
        char_pos = defaultdict(list)
        for i, c in enumerate(s):
            char_pos[c].append(i)

        count = 0
        for word, freq in word_count.items():
            prev = -1
            found = True
            for c in word:
                if c not in char_pos:
                    found = False
                    break
                idx = bisect_left(char_pos[c], prev + 1)
                if idx == len(char_pos[c]):
                    found = False
                    break
                prev = char_pos[c][idx]

            if found:
                count += freq

        return count
