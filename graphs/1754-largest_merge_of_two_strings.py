#1754. Largest Merge Of Two Strings
#Medium
#
#You are given two strings word1 and word2. You want to construct a string merge
#in the following way: while either word1 or word2 are non-empty, choose one of
#the following options:
#
#- If word1 is non-empty, append the first character in word1 to merge and delete
#  it from word1.
#- If word2 is non-empty, append the first character in word2 to merge and delete
#  it from word2.
#
#Return the lexicographically largest merge you can construct.
#
#Example 1:
#Input: word1 = "cabaa", word2 = "bcaaa"
#Output: "cbcabaaaaa"
#
#Example 2:
#Input: word1 = "abcabc", word2 = "abdcaba"
#Output: "abdcabcabcaba"
#
#Constraints:
#    1 <= word1.length, word2.length <= 3000
#    word1 and word2 consist only of lowercase English letters.

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        """
        Greedy: always take from string that is lexicographically larger.
        """
        result = []
        i, j = 0, 0
        n, m = len(word1), len(word2)

        while i < n and j < m:
            # Compare remaining suffixes
            if word1[i:] > word2[j:]:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1

        # Append remaining
        result.append(word1[i:])
        result.append(word2[j:])

        return ''.join(result)


class SolutionRecursive:
    def largestMerge(self, word1: str, word2: str) -> str:
        """
        Recursive with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def helper(i: int, j: int) -> str:
            if i == len(word1):
                return word2[j:]
            if j == len(word2):
                return word1[i:]

            if word1[i:] > word2[j:]:
                return word1[i] + helper(i + 1, j)
            else:
                return word2[j] + helper(i, j + 1)

        return helper(0, 0)


class SolutionIterative:
    def largestMerge(self, word1: str, word2: str) -> str:
        """
        Same logic with explicit index tracking.
        """
        merge = []
        p1, p2 = 0, 0

        while p1 < len(word1) or p2 < len(word2):
            if p1 >= len(word1):
                merge.append(word2[p2:])
                break
            elif p2 >= len(word2):
                merge.append(word1[p1:])
                break
            elif word1[p1:] > word2[p2:]:
                merge.append(word1[p1])
                p1 += 1
            else:
                merge.append(word2[p2])
                p2 += 1

        return ''.join(merge)
