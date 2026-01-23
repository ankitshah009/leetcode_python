#1081. Smallest Subsequence of Distinct Characters
#Medium
#
#Given a string s, return the lexicographically smallest subsequence of s
#that contains all the distinct characters of s exactly once.
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
#    1 <= s.length <= 1000
#    s consists of lowercase English letters.
#
#Note: This is the same as LeetCode 316. Remove Duplicate Letters.

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        Monotonic stack: Keep smallest lexicographic order.
        Only pop if character appears later.
        """
        last_occurrence = {c: i for i, c in enumerate(s)}
        in_stack = set()
        stack = []

        for i, c in enumerate(s):
            if c in in_stack:
                continue

            # Pop larger chars that appear later
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                in_stack.remove(stack.pop())

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)


class SolutionCounter:
    def smallestSubsequence(self, s: str) -> str:
        """Using counter for remaining occurrences"""
        from collections import Counter

        remaining = Counter(s)
        in_result = set()
        result = []

        for c in s:
            remaining[c] -= 1

            if c in in_result:
                continue

            while result and result[-1] > c and remaining[result[-1]] > 0:
                in_result.remove(result.pop())

            result.append(c)
            in_result.add(c)

        return ''.join(result)


class SolutionRecursive:
    def smallestSubsequence(self, s: str) -> str:
        """Recursive greedy approach"""
        if not s:
            return ""

        chars = set(s)

        for i, c in enumerate(s):
            # If remaining suffix contains all unique chars
            suffix = s[i:]
            if set(suffix) == chars:
                # Use this char and recurse on filtered suffix
                return c + self.smallestSubsequence(
                    suffix[1:].replace(c, '')
                )

        return ""
