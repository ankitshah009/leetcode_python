#316. Remove Duplicate Letters
#Medium
#
#Given a string s, remove duplicate letters so that every letter appears once and only once.
#You must make sure your result is the smallest in lexicographical order among all possible results.
#
#Example 1:
#Input: s = "bcabc"
#Output: "abc"
#
#Example 2:
#Input: s = "cbacdcbc"
#Output: "acdb"
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of lowercase English letters.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count remaining occurrences
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue

            # Remove characters that are greater than current and appear later
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                in_stack.remove(stack.pop())

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)
