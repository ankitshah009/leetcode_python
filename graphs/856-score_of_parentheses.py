#856. Score of Parentheses
#Medium
#
#Given a balanced parentheses string s, return the score of the string.
#
#The score of a balanced parentheses string is based on the following rule:
#- "()" has score 1.
#- AB has score A + B, where A and B are balanced parentheses strings.
#- (A) has score 2 * A, where A is a balanced parentheses string.
#
#Example 1:
#Input: s = "()"
#Output: 1
#
#Example 2:
#Input: s = "(())"
#Output: 2
#
#Example 3:
#Input: s = "()()"
#Output: 2
#
#Constraints:
#    2 <= s.length <= 50
#    s consists of only '(' and ')'.
#    s is a balanced parentheses string.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Stack-based: track scores at each depth level.
        """
        stack = [0]  # Stack of scores at each depth

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                # () = 1, (A) = 2*A
                score = max(1, 2 * inner)
                stack[-1] += score

        return stack[0]


class SolutionDepth:
    """Track depth: () at depth d contributes 2^d"""

    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        score = 0

        for i, c in enumerate(s):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                # Only count when closing a "()"
                if s[i - 1] == '(':
                    score += 1 << depth

        return score


class SolutionRecursive:
    """Recursive parsing"""

    def scoreOfParentheses(self, s: str) -> int:
        def parse(start, end):
            if end - start == 2:
                return 1

            # Find matching parenthesis for s[start]
            depth = 0
            for i in range(start, end):
                if s[i] == '(':
                    depth += 1
                else:
                    depth -= 1

                if depth == 0:
                    if i == end - 1:
                        # (A)
                        return 2 * parse(start + 1, end - 1)
                    else:
                        # AB
                        return parse(start, i + 1) + parse(i + 1, end)

            return 0

        return parse(0, len(s))


class SolutionDivide:
    """Divide and conquer"""

    def scoreOfParentheses(self, s: str) -> int:
        def score(s):
            if s == '()':
                return 1

            # Check if s = (A) or s = AB
            depth = 0
            for i, c in enumerate(s):
                depth += 1 if c == '(' else -1
                if depth == 0:
                    if i == len(s) - 1:
                        # s = (A)
                        return 2 * score(s[1:-1])
                    else:
                        # s = AB
                        return score(s[:i+1]) + score(s[i+1:])

            return 0

        return score(s)
