#20. Valid Parentheses
#Easy
#
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#determine if the input string is valid.
#
#An input string is valid if:
#1. Open brackets must be closed by the same type of brackets.
#2. Open brackets must be closed in the correct order.
#3. Every close bracket has a corresponding open bracket of the same type.
#
#Example 1:
#Input: s = "()"
#Output: true
#
#Example 2:
#Input: s = "()[]{}"
#Output: true
#
#Example 3:
#Input: s = "(]"
#Output: false
#
#Example 4:
#Input: s = "([])"
#Output: true
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack-based solution.
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)

        return len(stack) == 0


class SolutionReplace:
    def isValid(self, s: str) -> bool:
        """
        Repeatedly remove valid pairs.
        Less efficient but interesting approach.
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')

        return s == ''


class SolutionCounter:
    def isValid(self, s: str) -> bool:
        """
        Using stack with different approach.
        """
        stack = []
        open_brackets = {'(', '{', '['}
        close_to_open = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in close_to_open:
                if not stack:
                    return False
                if stack.pop() != close_to_open[char]:
                    return False

        return not stack


class SolutionAlternative:
    def isValid(self, s: str) -> bool:
        """
        Push corresponding closing bracket instead.
        """
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in mapping:
                # Push expected closing bracket
                stack.append(mapping[char])
            elif not stack or stack.pop() != char:
                return False

        return not stack
