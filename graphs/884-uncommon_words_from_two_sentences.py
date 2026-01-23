#884. Uncommon Words from Two Sentences
#Easy
#
#A sentence is a string of single-space separated words where each word consists
#only of lowercase letters.
#
#A word is uncommon if it appears exactly once in one of the sentences, and does
#not appear in the other sentence.
#
#Given two sentences s1 and s2, return a list of all the uncommon words. You may
#return the answer in any order.
#
#Example 1:
#Input: s1 = "this apple is sweet", s2 = "this apple is sour"
#Output: ["sweet","sour"]
#
#Example 2:
#Input: s1 = "apple apple", s2 = "banana"
#Output: ["banana"]
#
#Constraints:
#    1 <= s1.length, s2.length <= 200
#    s1 and s2 consist of lowercase English letters and spaces.
#    s1 and s2 do not have leading or trailing spaces.
#    All the words in s1 and s2 are separated by a single space.

from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        """
        A word is uncommon if it appears exactly once in both sentences combined.
        """
        count = Counter(s1.split() + s2.split())
        return [word for word, cnt in count.items() if cnt == 1]


class SolutionExplicit:
    """More explicit logic"""

    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        count1 = Counter(s1.split())
        count2 = Counter(s2.split())

        result = []

        # Words appearing exactly once in s1 and not in s2
        for word, cnt in count1.items():
            if cnt == 1 and word not in count2:
                result.append(word)

        # Words appearing exactly once in s2 and not in s1
        for word, cnt in count2.items():
            if cnt == 1 and word not in count1:
                result.append(word)

        return result


class SolutionSet:
    """Using set operations"""

    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words1 = s1.split()
        words2 = s2.split()

        # Words that appear more than once
        duplicates = set()
        seen = set()

        for word in words1 + words2:
            if word in seen:
                duplicates.add(word)
            seen.add(word)

        # Uncommon = seen exactly once
        return [w for w in seen if w not in duplicates]
