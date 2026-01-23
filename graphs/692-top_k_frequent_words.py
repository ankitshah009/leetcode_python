#692. Top K Frequent Words
#Medium
#
#Given an array of strings words and an integer k, return the k most frequent
#strings.
#
#Return the answer sorted by the frequency from highest to lowest. Sort the
#words with the same frequency by their lexicographical order.
#
#Example 1:
#Input: words = ["i","love","leetcode","i","love","coding"], k = 2
#Output: ["i","love"]
#Explanation: "i" and "love" are the two most frequent words.
#Note that "i" comes before "love" due to a lower alphabetical order.
#
#Example 2:
#Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"],
#k = 4
#Output: ["the","is","sunny","day"]
#Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#Constraints:
#    1 <= words.length <= 500
#    1 <= words[i].length <= 10
#    words[i] consists of lowercase English letters.
#    k is in the range [1, The number of unique words[i]]

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        Count frequencies, sort by (-count, word), take top k.
        """
        count = Counter(words)
        return sorted(count.keys(), key=lambda x: (-count[x], x))[:k]


class SolutionHeap:
    """Min-heap approach for O(n log k) complexity"""

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)

        # Use negative count for max-heap behavior
        # Custom wrapper for lexicographic comparison when counts equal
        class Word:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            def __lt__(self, other):
                if self.freq != other.freq:
                    return self.freq < other.freq
                return self.word > other.word  # Reverse for min-heap

        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, Word(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]


class SolutionBucketSort:
    """Bucket sort for O(n) average complexity"""

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        n = len(words)

        # Buckets: bucket[i] contains words with frequency i
        buckets = [[] for _ in range(n + 1)]

        for word, freq in count.items():
            buckets[freq].append(word)

        result = []
        for freq in range(n, 0, -1):
            if buckets[freq]:
                buckets[freq].sort()  # Lexicographic order
                for word in buckets[freq]:
                    result.append(word)
                    if len(result) == k:
                        return result

        return result
