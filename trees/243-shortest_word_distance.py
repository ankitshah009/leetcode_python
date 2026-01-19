#243. Shortest Word Distance
#Easy
#
#Given an array of strings wordsDict and two different strings that already
#exist in the array word1 and word2, return the shortest distance between these
#two words in the list.
#
#Example 1:
#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
#Output: 3
#
#Example 2:
#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
#Output: 1
#
#Constraints:
#    2 <= wordsDict.length <= 3 * 10^4
#    1 <= wordsDict[i].length <= 10
#    wordsDict[i] consists of lowercase English letters.
#    word1 and word2 are in wordsDict.
#    word1 != word2

from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """One pass - O(n) time, O(1) space"""
        idx1 = idx2 = -1
        min_dist = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
            elif word == word2:
                idx2 = i

            if idx1 != -1 and idx2 != -1:
                min_dist = min(min_dist, abs(idx1 - idx2))

        return min_dist


class SolutionTwoLists:
    """Store all indices then find minimum difference"""

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indices1 = [i for i, word in enumerate(wordsDict) if word == word1]
        indices2 = [i for i, word in enumerate(wordsDict) if word == word2]

        min_dist = float('inf')
        i = j = 0

        # Two pointer on sorted lists
        while i < len(indices1) and j < len(indices2):
            min_dist = min(min_dist, abs(indices1[i] - indices2[j]))

            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        return min_dist


class SolutionBruteForce:
    """O(n^2) brute force"""

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2:
                        min_dist = min(min_dist, abs(i - j))

        return min_dist
