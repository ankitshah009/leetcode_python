#734. Sentence Similarity
#Easy
#
#We can represent a sentence as an array of words, for example, the sentence
#"I am happy with leetcode" can be represented as arr = ["I","am","happy",
#"with","leetcode"].
#
#Given two sentences sentence1 and sentence2 each represented as a string array
#and given an array of string pairs similarPairs where similarPairs[i] =
#[xi, yi] indicates that the two words xi and yi are similar.
#
#Return true if sentence1 and sentence2 are similar, or false if they are not.
#
#Two sentences are similar if:
#- They have the same length (i.e., the same number of words)
#- sentence1[i] and sentence2[i] are similar.
#
#Notice that a word is always similar to itself, also notice that the similarity
#relation is not transitive. For example, if the words a and b are similar, and
#the words b and c are similar, a and c are not necessarily similar.
#
#Example 1:
#Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama",
#"talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
#Output: true
#Explanation: The two sentences have the same length and each word i of
#sentence1 is also similar to the corresponding word in sentence2.
#
#Example 2:
#Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
#Output: true
#Explanation: A word is similar to itself.
#
#Example 3:
#Input: sentence1 = ["great"], sentence2 = ["doubtful"], similarPairs =
#[["great","fine"]]
#Output: false
#
#Constraints:
#    1 <= sentence1.length, sentence2.length <= 1000
#    1 <= sentence1[i].length, sentence2[i].length <= 20
#    sentence1[i] and sentence2[i] consist of English letters.
#    0 <= similarPairs.length <= 1000
#    similarPairs[i].length == 2
#    1 <= xi.length, yi.length <= 20

class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str],
                            similarPairs: list[list[str]]) -> bool:
        """
        Build a set of similar pairs and check each word pair.
        """
        if len(sentence1) != len(sentence2):
            return False

        # Build similarity set (both directions)
        similar = set()
        for w1, w2 in similarPairs:
            similar.add((w1, w2))
            similar.add((w2, w1))

        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and (w1, w2) not in similar:
                return False

        return True


class SolutionDict:
    """Using dictionary for similarity lookup"""

    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str],
                            similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        from collections import defaultdict
        similar = defaultdict(set)

        for w1, w2 in similarPairs:
            similar[w1].add(w2)
            similar[w2].add(w1)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and w2 not in similar[w1]:
                return False

        return True


class SolutionCompact:
    """Compact solution"""

    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str],
                            similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pairs = set(map(tuple, similarPairs)) | set(map(lambda x: (x[1], x[0]), similarPairs))

        return all(
            w1 == w2 or (w1, w2) in pairs
            for w1, w2 in zip(sentence1, sentence2)
        )
