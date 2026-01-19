#316. Remove Duplicate Letters
#Medium
#
#Given a string s, remove duplicate letters so that every letter appears once
#and only once. You must make sure your result is the smallest in
#lexicographical order among all possible results.
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

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Monotonic stack with last occurrence tracking"""
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue

            # Pop characters that are greater than current and will appear later
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return ''.join(stack)


class SolutionCounter:
    """Using counter for remaining occurrences"""

    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        in_stack = set()

        for c in s:
            count[c] -= 1

            if c in in_stack:
                continue

            while stack and stack[-1] > c and count[stack[-1]] > 0:
                in_stack.remove(stack.pop())

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)


class SolutionRecursive:
    """Recursive approach"""

    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""

        # Find the smallest character that has all other chars after it
        count = Counter(s)

        for i, c in enumerate(s):
            if all(count[ch] > 0 for ch in set(s)):
                # c is valid starting point
                if c == min(s[i:]):
                    # Remove all occurrences of c and recurse
                    return c + self.removeDuplicateLetters(s[i+1:].replace(c, ''))
            count[c] -= 1

        return ""
