#1190. Reverse Substrings Between Each Pair of Parentheses
#Medium
#
#You are given a string s that consists of lower case English letters and brackets.
#
#Reverse the strings in each pair of matching parentheses, starting from the
#innermost one.
#
#Your result should not contain any brackets.
#
#Example 1:
#Input: s = "(abcd)"
#Output: "dcba"
#
#Example 2:
#Input: s = "(u(love)i)"
#Output: "iloveu"
#Explanation: The substring "love" is reversed first, then the whole string is reversed.
#
#Example 3:
#Input: s = "(ed(et(oc))el)"
#Output: "leetcode"
#Explanation: First, we reverse "oc", to get "co".
#Then we reverse "etco", to get "octe".
#Finally we reverse "octe", to get "etco", then the final answer.
#
#Constraints:
#    1 <= s.length <= 2000
#    s only contains lower case English characters and parentheses.
#    It is guaranteed that all parentheses are balanced.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        Stack-based approach: Use stack to track substrings.
        When we see ')', pop and reverse, then append to previous level.
        """
        stack = [[]]  # Stack of character lists

        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                # Pop, reverse, and append to previous level
                top = stack.pop()
                stack[-1].extend(reversed(top))
            else:
                stack[-1].append(c)

        return ''.join(stack[0])


class SolutionWormhole:
    def reverseParentheses(self, s: str) -> str:
        """
        O(n) wormhole/portal approach.
        Pre-compute matching parentheses, then traverse with direction changes.
        """
        n = len(s)

        # Find matching parentheses
        pair = [0] * n
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        # Traverse with direction changes at parentheses
        result = []
        i = 0
        direction = 1  # 1 = forward, -1 = backward

        while 0 <= i < n:
            if s[i] in '()':
                # Jump to matching parenthesis and reverse direction
                i = pair[i]
                direction = -direction
            else:
                result.append(s[i])
            i += direction

        return ''.join(result)


class SolutionRecursive:
    def reverseParentheses(self, s: str) -> str:
        """Recursive approach"""
        def process(start):
            result = []
            i = start

            while i < len(s):
                if s[i] == '(':
                    # Recursively process inner part
                    inner, end = process(i + 1)
                    result.extend(reversed(inner))
                    i = end
                elif s[i] == ')':
                    return result, i + 1
                else:
                    result.append(s[i])
                    i += 1

            return result, i

        chars, _ = process(0)
        return ''.join(chars)
