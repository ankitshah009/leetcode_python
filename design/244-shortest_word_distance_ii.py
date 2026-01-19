#244. Shortest Word Distance II
#Medium
#
#Design a data structure that will be initialized with a string array, and then
#it should answer queries of the shortest distance between two different strings
#from the array.
#
#Implement the WordDistance class:
#    WordDistance(String[] wordsDict) Initializes the object with the strings
#    array wordsDict.
#    int shortest(String word1, String word2) Returns the shortest distance
#    between word1 and word2 in the array wordsDict.
#
#Example 1:
#Input
#["WordDistance", "shortest", "shortest"]
#[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
#Output
#[null, 3, 1]
#
#Explanation
#WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
#wordDistance.shortest("coding", "practice"); // return 3
#wordDistance.shortest("makes", "coding");    // return 1
#
#Constraints:
#    1 <= wordsDict.length <= 3 * 10^4
#    1 <= wordsDict[i].length <= 10
#    wordsDict[i] consists of lowercase English letters.
#    word1 and word2 are in wordsDict.
#    word1 != word2
#    At most 5000 calls will be made to shortest.

from collections import defaultdict

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # Store indices for each word
        self.word_indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # Two pointer approach on sorted index lists
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]

        i, j = 0, 0
        min_dist = float('inf')

        while i < len(indices1) and j < len(indices2):
            min_dist = min(min_dist, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        return min_dist


class WordDistanceWithCache:
    """Caches results for repeated queries"""

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)
        self.cache = {}

    def shortest(self, word1: str, word2: str) -> int:
        # Create cache key (order doesn't matter)
        key = tuple(sorted([word1, word2]))
        if key in self.cache:
            return self.cache[key]

        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]

        i, j = 0, 0
        min_dist = float('inf')

        while i < len(indices1) and j < len(indices2):
            min_dist = min(min_dist, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        self.cache[key] = min_dist
        return min_dist
