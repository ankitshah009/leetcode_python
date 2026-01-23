#1528. Shuffle String
#Easy
#
#You are given a string s and an integer array indices of the same length. The
#string s will be shuffled such that the character at the ith position moves
#to indices[i] in the shuffled string.
#
#Return the shuffled string.
#
#Example 1:
#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
#
#Example 2:
#Input: s = "abc", indices = [0,1,2]
#Output: "abc"
#Explanation: After shuffling, each character remains in its position.
#
#Constraints:
#    s.length == indices.length == n
#    1 <= n <= 100
#    s consists of only lowercase English letters.
#    0 <= indices[i] < n
#    All values of indices are unique.

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Place each character at its target position.
        """
        n = len(s)
        result = [''] * n

        for i, char in enumerate(s):
            result[indices[i]] = char

        return ''.join(result)


class SolutionDict:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """Using dictionary"""
        mapping = {idx: char for idx, char in zip(indices, s)}
        return ''.join(mapping[i] for i in range(len(s)))


class SolutionSort:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """Sort by indices and extract characters"""
        pairs = sorted(zip(indices, s))
        return ''.join(char for _, char in pairs)


class SolutionInPlace:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        In-place cyclic swapping (for mutable sequences).
        """
        chars = list(s)
        indices = indices.copy()

        for i in range(len(chars)):
            while indices[i] != i:
                target = indices[i]
                # Swap characters
                chars[i], chars[target] = chars[target], chars[i]
                # Swap indices
                indices[i], indices[target] = indices[target], indices[i]

        return ''.join(chars)


class SolutionComprehension:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """Using enumerate and list comprehension"""
        result = [''] * len(s)
        for i, idx in enumerate(indices):
            result[idx] = s[i]
        return ''.join(result)
