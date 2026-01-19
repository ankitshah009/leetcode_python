#245. Shortest Word Distance III
#Medium
#
#Given an array of strings wordsDict and two strings that already exist in the
#array word1 and word2, return the shortest distance between the occurrence of
#these two words in the list.
#
#Note that word1 and word2 may be the same. It is guaranteed that they represent
#two individual words in the list.
#
#Example 1:
#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
#Output: 1
#
#Example 2:
#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
#Output: 3
#
#Constraints:
#    1 <= wordsDict.length <= 10^5
#    1 <= wordsDict[i].length <= 10
#    wordsDict[i] consists of lowercase English letters.
#    word1 and word2 are in wordsDict.

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = -1, -1
        min_dist = float('inf')
        same_word = word1 == word2

        for i, word in enumerate(wordsDict):
            if word == word1:
                if same_word:
                    # For same word, update idx2 first then idx1
                    idx2 = idx1
                    idx1 = i
                else:
                    idx1 = i

            elif word == word2:
                idx2 = i

            if idx1 != -1 and idx2 != -1:
                min_dist = min(min_dist, abs(idx1 - idx2))

        return min_dist

    # Alternative with single pointer tracking
    def shortestWordDistanceAlt(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last_idx = -1
        min_dist = float('inf')
        same_word = word1 == word2

        for i, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if last_idx != -1:
                    if same_word or wordsDict[last_idx] != word:
                        min_dist = min(min_dist, i - last_idx)
                last_idx = i

        return min_dist
