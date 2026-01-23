#1047. Remove All Adjacent Duplicates In String
#Easy
#
#You are given a string s consisting of lowercase English letters.
#A duplicate removal consists of choosing two adjacent and equal letters
#and removing them.
#
#We repeatedly make duplicate removals on s until we no longer can.
#
#Return the final string after all such duplicate removals have been made.
#It can be proven that the answer is unique.
#
#Example 1:
#Input: s = "abbaca"
#Output: "ca"
#Explanation:
#In "abbaca" we can remove "bb" since the letters are adjacent and equal.
#This leaves "aaca" where "aa" is now adjacent and can be removed.
#This results in "ca".
#
#Example 2:
#Input: s = "azxxzy"
#Output: "ay"
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of lowercase English letters.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Stack-based approach.
        If current char equals stack top, pop; otherwise push.
        """
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


class SolutionTwoPointer:
    def removeDuplicates(self, s: str) -> str:
        """In-place using two pointers (conceptually)"""
        result = list(s)
        i = 0  # Write pointer

        for j in range(len(s)):
            result[i] = s[j]
            if i > 0 and result[i] == result[i - 1]:
                i -= 2
            i += 1

        return ''.join(result[:i])


class SolutionRecursive:
    def removeDuplicates(self, s: str) -> str:
        """Recursive approach - less efficient"""
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                return self.removeDuplicates(s[:i] + s[i + 2:])
            i += 1
        return s
