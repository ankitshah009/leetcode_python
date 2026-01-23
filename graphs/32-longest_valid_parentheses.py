#32. Longest Valid Parentheses
#Hard
#
#Given a string containing just the characters '(' and ')', return the length of
#the longest valid (well-formed) parentheses substring.
#
#Example 1:
#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".
#
#Example 2:
#Input: s = ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()".
#
#Example 3:
#Input: s = ""
#Output: 0
#
#Constraints:
#    0 <= s.length <= 3 * 10^4
#    s[i] is '(', or ')'.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Stack-based approach - O(n) time, O(n) space.
        Stack stores indices of unmatched parentheses.
        """
        stack = [-1]  # Base for length calculation
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # No matching '(', push current index as new base
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len


class SolutionDP:
    def longestValidParentheses(self, s: str) -> int:
        """
        Dynamic Programming - O(n) time, O(n) space.
        dp[i] = length of longest valid substring ending at i.
        """
        n = len(s)
        if n < 2:
            return 0

        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case: ...()
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif dp[i - 1] > 0:
                    # Case: ...))
                    matching = i - dp[i - 1] - 1
                    if matching >= 0 and s[matching] == '(':
                        dp[i] = dp[i - 1] + 2
                        if matching >= 1:
                            dp[i] += dp[matching - 1]

                max_len = max(max_len, dp[i])

        return max_len


class SolutionTwoPass:
    def longestValidParentheses(self, s: str) -> int:
        """
        Two passes - O(n) time, O(1) space.
        Left to right, then right to left.
        """
        max_len = 0

        # Left to right
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left
        left = right = 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len


class SolutionBruteForce:
    def longestValidParentheses(self, s: str) -> int:
        """
        Brute force - check all substrings - O(n^3).
        """
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i + 2, n + 1, 2):  # Only even lengths
                if is_valid(s[i:j]):
                    max_len = max(max_len, j - i)

        return max_len
