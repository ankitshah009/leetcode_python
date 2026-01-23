#890. Find and Replace Pattern
#Medium
#
#Given a list of strings words and a string pattern, return a list of words[i]
#that match pattern. You may return the answer in any order.
#
#A word matches the pattern if there exists a permutation of letters p so that
#after replacing every letter x in the pattern with p(x), we get the desired word.
#
#Recall that a permutation of letters is a bijection from letters to letters:
#every letter maps to another letter, and no two letters map to the same letter.
#
#Example 1:
#Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
#Output: ["mee","aqq"]
#
#Example 2:
#Input: words = ["a","b","c"], pattern = "a"
#Output: ["a","b","c"]
#
#Constraints:
#    1 <= pattern.length <= 20
#    1 <= words.length <= 50
#    words[i].length == pattern.length
#    pattern and words[i] are lowercase English letters.

class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        """
        Normalize both word and pattern to canonical form.
        Two strings match if their canonical forms are equal.
        """
        def normalize(s):
            mapping = {}
            result = []
            for c in s:
                if c not in mapping:
                    mapping[c] = len(mapping)
                result.append(mapping[c])
            return tuple(result)

        pattern_norm = normalize(pattern)
        return [word for word in words if normalize(word) == pattern_norm]


class SolutionBijection:
    """Check bijection directly"""

    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def matches(word, pattern):
            if len(word) != len(pattern):
                return False

            w_to_p = {}
            p_to_w = {}

            for w, p in zip(word, pattern):
                if w in w_to_p:
                    if w_to_p[w] != p:
                        return False
                else:
                    w_to_p[w] = p

                if p in p_to_w:
                    if p_to_w[p] != w:
                        return False
                else:
                    p_to_w[p] = w

            return True

        return [word for word in words if matches(word, pattern)]


class SolutionZip:
    """Using zip for mapping check"""

    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if m1.setdefault(w, p) != p or m2.setdefault(p, w) != w:
                    return False
            return True

        return [w for w in words if match(w)]
