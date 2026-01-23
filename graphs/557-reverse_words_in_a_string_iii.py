#557. Reverse Words in a String III
#Easy
#
#Given a string s, reverse the order of characters in each word within a sentence
#while still preserving whitespace and initial word order.
#
#Example 1:
#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
#
#Example 2:
#Input: s = "Mr Ding"
#Output: "rM gniD"
#
#Constraints:
#    1 <= s.length <= 5 * 10^4
#    s contains printable ASCII characters.
#    s does not contain any leading or trailing spaces.
#    There is at least one word in s.
#    All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        """Split, reverse each word, join"""
        return ' '.join(word[::-1] for word in s.split())


class SolutionTwoPointers:
    """In-place reversal simulation"""

    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                # Reverse word from start to i-1
                left, right = start, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = i + 1

        return ''.join(chars)


class SolutionMap:
    """Using map function"""

    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda w: w[::-1], s.split(' ')))


class SolutionStack:
    """Using stack for each word"""

    def reverseWords(self, s: str) -> str:
        result = []
        stack = []

        for c in s:
            if c == ' ':
                while stack:
                    result.append(stack.pop())
                result.append(' ')
            else:
                stack.append(c)

        while stack:
            result.append(stack.pop())

        return ''.join(result)
