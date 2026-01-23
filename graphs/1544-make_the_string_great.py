#1544. Make The String Great
#Easy
#
#Given a string s of lower and upper case English letters.
#
#A good string is a string which doesn't have two adjacent characters s[i] and
#s[i + 1] where:
#- 0 <= i <= s.length - 2
#- s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case
#  or vice-versa.
#
#To make the string good, you can choose two adjacent characters that make the
#string bad and remove them. You can keep doing this until the string becomes good.
#
#Return the string after making it good. The answer is guaranteed to be unique
#under the given constraints.
#
#Notice that an empty string is also good.
#
#Example 1:
#Input: s = "leEeetcode"
#Output: "leetcode"
#Explanation: In the first step, either you choose i = 1 or i = 2, both will
#result in "leeetcode" to be reduced to "leetcode".
#
#Example 2:
#Input: s = "abBAcC"
#Output: ""
#Explanation: We have many possible scenarios, and all lead to the same answer.
#"abBAcC" --> "aAcC" --> "cC" --> ""
#
#Example 3:
#Input: s = "s"
#Output: "s"
#
#Constraints:
#    1 <= s.length <= 100
#    s contains only lower and upper case English letters.

class Solution:
    def makeGood(self, s: str) -> str:
        """
        Stack-based approach: Remove adjacent bad pairs.
        Two chars are bad if they're same letter but different case.
        """
        stack = []

        for c in s:
            if stack and self.is_bad_pair(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

    def is_bad_pair(self, a: str, b: str) -> bool:
        return a.lower() == b.lower() and a != b


class SolutionASCII:
    def makeGood(self, s: str) -> str:
        """
        Using ASCII difference to detect bad pairs.
        'a' and 'A' differ by 32 in ASCII.
        """
        stack = []

        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


class SolutionRecursive:
    def makeGood(self, s: str) -> str:
        """
        Recursive approach (less efficient but intuitive).
        """
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood(s[:i] + s[i + 2:])
        return s


class SolutionIterative:
    def makeGood(self, s: str) -> str:
        """
        Iterative approach with repeated passes.
        """
        result = list(s)

        changed = True
        while changed:
            changed = False
            new_result = []
            i = 0
            while i < len(result):
                if i + 1 < len(result) and abs(ord(result[i]) - ord(result[i + 1])) == 32:
                    i += 2
                    changed = True
                else:
                    new_result.append(result[i])
                    i += 1
            result = new_result

        return ''.join(result)


class SolutionSwapCase:
    def makeGood(self, s: str) -> str:
        """
        Using swapcase for comparison.
        """
        stack = []

        for c in s:
            if stack and stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
