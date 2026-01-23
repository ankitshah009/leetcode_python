#893. Groups of Special-Equivalent Strings
#Medium
#
#You are given an array of strings of the same length words.
#
#In one move, you can swap any two even indexed characters or any two odd indexed
#characters of a string.
#
#Two strings are special-equivalent if after any number of moves, word1 == word2.
#
#A group of special-equivalent strings from words is a non-empty subset of words
#such that:
#- Every pair of strings in the group are special equivalent, and
#- The group is the largest size possible.
#
#Return the number of groups of special-equivalent strings from words.
#
#Example 1:
#Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
#Output: 3
#Explanation: Groups are ["abcd","cdab","cbad"], ["xyzz","zzxy"], ["zzyx"].
#
#Example 2:
#Input: words = ["abc","acb","bac","bca","cab","cba"]
#Output: 3
#
#Constraints:
#    1 <= words.length <= 1000
#    1 <= words[i].length <= 20
#    words[i] consist of lowercase English letters.
#    All the strings are of the same length.

class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        """
        Two words are special-equivalent if sorted even-indexed chars and
        sorted odd-indexed chars are the same.
        """
        def signature(word):
            even = ''.join(sorted(word[::2]))
            odd = ''.join(sorted(word[1::2]))
            return (even, odd)

        return len(set(signature(word) for word in words))


class SolutionCounter:
    """Using Counter for signature"""

    def numSpecialEquivGroups(self, words: list[str]) -> int:
        from collections import Counter

        def signature(word):
            even = tuple(sorted(word[::2]))
            odd = tuple(sorted(word[1::2]))
            return (even, odd)

        return len(set(signature(word) for word in words))


class SolutionExplicit:
    """More explicit indexing"""

    def numSpecialEquivGroups(self, words: list[str]) -> int:
        groups = set()

        for word in words:
            even_chars = sorted(word[i] for i in range(0, len(word), 2))
            odd_chars = sorted(word[i] for i in range(1, len(word), 2))
            groups.add((tuple(even_chars), tuple(odd_chars)))

        return len(groups)
