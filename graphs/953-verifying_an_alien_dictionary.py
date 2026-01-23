#953. Verifying an Alien Dictionary
#Easy
#
#In an alien language, surprisingly, they also use English lowercase letters,
#but possibly in a different order. The order of the alphabet is some
#permutation of lowercase letters.
#
#Given a sequence of words written in the alien language, and the order of the
#alphabet, return true if and only if the given words are sorted
#lexicographically in this alien language.
#
#Example 1:
#Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
#Output: true
#
#Example 2:
#Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
#Output: false
#
#Example 3:
#Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
#Output: false
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 20
#    order.length == 26
#    All characters in words[i] and order are English lowercase letters.

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """
        Create order mapping and compare adjacent words.
        """
        order_map = {c: i for i, c in enumerate(order)}

        def is_sorted(word1: str, word2: str) -> bool:
            for c1, c2 in zip(word1, word2):
                if order_map[c1] < order_map[c2]:
                    return True
                if order_map[c1] > order_map[c2]:
                    return False
            # One is prefix of other
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False

        return True


class SolutionTransform:
    """Transform words and use normal comparison"""

    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {c: chr(ord('a') + i) for i, c in enumerate(order)}

        def transform(word):
            return ''.join(order_map[c] for c in word)

        transformed = [transform(w) for w in words]
        return transformed == sorted(transformed)


class SolutionCompact:
    """Compact solution"""

    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_idx = {c: i for i, c in enumerate(order)}

        def compare(w1, w2):
            for c1, c2 in zip(w1, w2):
                if order_idx[c1] != order_idx[c2]:
                    return order_idx[c1] < order_idx[c2]
            return len(w1) <= len(w2)

        return all(compare(words[i], words[i + 1]) for i in range(len(words) - 1))
