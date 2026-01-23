#1813. Sentence Similarity III
#Medium
#
#A sentence is a list of words that are separated by a single space with no
#leading or trailing spaces. For example, "Hello World", "HELLO", "hello world
#hello world" are all sentences.
#
#Words consist of only uppercase and lowercase English letters.
#
#Two sentences sentence1 and sentence2 are similar if it is possible to insert
#an arbitrary sentence (possibly empty) inside one of these sentences such that
#the two sentences become equal.
#
#Example 1:
#Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
#Output: true
#Explanation: sentence2 can become sentence1 by inserting "name is".
#
#Example 2:
#Input: sentence1 = "of", sentence2 = "A lot of words"
#Output: false
#
#Example 3:
#Input: sentence1 = "Eating right now", sentence2 = "Eating"
#Output: true
#
#Constraints:
#    1 <= sentence1.length, sentence2.length <= 100
#    sentence1 and sentence2 consist of lowercase and uppercase English letters
#    and spaces.
#    The words in sentence1 and sentence2 are separated by a single space.

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        Match from both ends.
        """
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Make words1 the shorter one
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        n1, n2 = len(words1), len(words2)

        # Match from start
        left = 0
        while left < n1 and words1[left] == words2[left]:
            left += 1

        # Match from end
        right = 0
        while right < n1 - left and words1[n1 - 1 - right] == words2[n2 - 1 - right]:
            right += 1

        return left + right >= n1


class SolutionDeque:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        Using deques to pop from both ends.
        """
        from collections import deque

        d1 = deque(sentence1.split())
        d2 = deque(sentence2.split())

        # Pop matching from front
        while d1 and d2 and d1[0] == d2[0]:
            d1.popleft()
            d2.popleft()

        # Pop matching from back
        while d1 and d2 and d1[-1] == d2[-1]:
            d1.pop()
            d2.pop()

        # One must be empty for similarity
        return not d1 or not d2


class SolutionTwoPointers:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        Explicit two-pointer approach.
        """
        w1 = sentence1.split()
        w2 = sentence2.split()

        if len(w1) > len(w2):
            w1, w2 = w2, w1

        i, j = 0, len(w1) - 1
        k, l = 0, len(w2) - 1

        # Match from start
        while i <= j and w1[i] == w2[k]:
            i += 1
            k += 1

        # Match from end
        while i <= j and w1[j] == w2[l]:
            j -= 1
            l -= 1

        return i > j
