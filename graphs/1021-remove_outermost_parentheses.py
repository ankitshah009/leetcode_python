#1021. Remove Outermost Parentheses
#Easy
#
#A valid parentheses string is either empty "", "(" + A + ")", or A + B,
#where A and B are valid parentheses strings, and + represents string
#concatenation.
#
#A valid parentheses string s is primitive if it is nonempty, and there
#does not exist a way to split it into s = A + B, with A and B nonempty
#valid parentheses strings.
#
#Given a valid parentheses string s, consider its primitive decomposition:
#s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
#
#Return s after removing the outermost parentheses of every primitive string
#in the primitive decomposition of s.
#
#Example 1:
#Input: s = "(()())(())"
#Output: "()()()"
#Explanation:
#The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
#After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
#
#Example 2:
#Input: s = "(()())(())(()(()))"
#Output: "()()()()(())"
#
#Example 3:
#Input: s = "()()"
#Output: ""
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is either '(' or ')'.
#    s is a valid parentheses string.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Track depth; include chars when depth > 0 after processing.
        """
        result = []
        depth = 0

        for c in s:
            if c == '(':
                if depth > 0:
                    result.append(c)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(c)

        return ''.join(result)


class SolutionPrimitive:
    def removeOuterParentheses(self, s: str) -> str:
        """Find each primitive and remove outer parentheses"""
        result = []
        start = 0
        depth = 0

        for i, c in enumerate(s):
            depth += 1 if c == '(' else -1
            if depth == 0:
                # Found a primitive from start to i
                result.append(s[start+1:i])
                start = i + 1

        return ''.join(result)
