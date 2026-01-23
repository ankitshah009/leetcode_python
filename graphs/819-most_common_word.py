#819. Most Common Word
#Easy
#
#Given a string paragraph and a string array of the banned words banned, return
#the most frequent word that is not banned. It is guaranteed there is at least
#one word that is not banned, and that the answer is unique.
#
#The words in paragraph are case-insensitive and the answer should be returned
#in lowercase.
#
#Example 1:
#Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
#Output: "ball"
#Explanation:
#"hit" occurs 3 times, but it's banned.
#"ball" occurs twice (and no other word does), so it's the most frequent non-banned word.
#
#Example 2:
#Input: paragraph = "a.", banned = []
#Output: "a"
#
#Constraints:
#    1 <= paragraph.length <= 1000
#    paragraph consists of English letters, space ' ', or one of "!?',;.".
#    0 <= banned.length <= 100
#    1 <= banned[i].length <= 10
#    banned[i] consists of only lowercase English letters.

import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        Extract words, filter banned, find most common.
        """
        # Extract words (letters only)
        words = re.findall(r'[a-zA-Z]+', paragraph.lower())

        banned_set = set(banned)

        # Count non-banned words
        word_count = Counter(w for w in words if w not in banned_set)

        return word_count.most_common(1)[0][0]


class SolutionManual:
    """Manual parsing without regex"""

    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        from collections import defaultdict

        banned_set = set(banned)
        word_count = defaultdict(int)

        word = []
        for c in paragraph.lower() + ' ':
            if c.isalpha():
                word.append(c)
            elif word:
                w = ''.join(word)
                if w not in banned_set:
                    word_count[w] += 1
                word = []

        return max(word_count.keys(), key=lambda w: word_count[w])


class SolutionReplace:
    """Using string replacement"""

    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Replace non-letters with spaces
        normalized = ''.join(c.lower() if c.isalpha() else ' ' for c in paragraph)
        words = normalized.split()

        banned_set = set(banned)
        count = Counter(w for w in words if w not in banned_set)

        return count.most_common(1)[0][0]
