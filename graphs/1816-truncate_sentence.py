#1816. Truncate Sentence
#Easy
#
#A sentence is a list of words that are separated by a single space with no
#leading or trailing spaces. Each of the words consists of only uppercase and
#lowercase English letters (no punctuation).
#
#For example, "Hello World", "HELLO", and "hello world hello world" are all
#sentences.
#
#You are given a sentence s and an integer k. You want to truncate s such that
#it contains only the first k words. Return s after truncating it.
#
#Example 1:
#Input: s = "Hello how are you Contestant", k = 4
#Output: "Hello how are you"
#
#Example 2:
#Input: s = "What is the solution to this problem", k = 4
#Output: "What is the solution"
#
#Example 3:
#Input: s = "chopper is not a, but a robot", k = 5
#Output: "chopper is not a, but"
#
#Constraints:
#    1 <= s.length <= 500
#    k is in the range [1, the number of words in s].
#    s consist of only lowercase and uppercase English letters and spaces.
#    The words in s are separated by a single space.
#    There are no leading or trailing spaces.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Split and join first k words.
        """
        return ' '.join(s.split()[:k])


class SolutionManual:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Find kth space manually.
        """
        count = 0
        for i, c in enumerate(s):
            if c == ' ':
                count += 1
                if count == k:
                    return s[:i]
        return s


class SolutionIndex:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Using string index method.
        """
        pos = 0
        for _ in range(k):
            pos = s.find(' ', pos)
            if pos == -1:
                return s
            pos += 1
        return s[:pos - 1]
