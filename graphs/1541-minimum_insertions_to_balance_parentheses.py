#1541. Minimum Insertions to Balance a Parentheses String
#Medium
#
#Given a parentheses string s containing only the characters '(' and ')'. A
#parentheses string is balanced if:
#- Any left parenthesis '(' must have a corresponding two consecutive right
#  parenthesis '))'.
#- Left parenthesis '(' must go before the corresponding two consecutive right
#  parenthesis '))'.
#
#In other words, we treat '(' as an opening parenthesis and '))' as a closing
#parenthesis.
#
#For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and
#"(()))" are not balanced.
#
#You can insert the characters '(' and ')' at any position of the string to
#balance it if needed.
#
#Return the minimum number of insertions needed to make s balanced.
#
#Example 1:
#Input: s = "(()))"
#Output: 1
#Explanation: The second '(' has two matching '))', but the first '(' has only ')'
#matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
#
#Example 2:
#Input: s = "())"
#Output: 0
#Explanation: The string is already balanced.
#
#Example 3:
#Input: s = "))())("
#Output: 3
#Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of '(' and ')' only.

class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Track unmatched '(' and unmatched ')' that need pairing.

        Each '(' needs '))' to close.
        """
        insertions = 0
        open_count = 0  # Unmatched '('

        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                # s[i] == ')'
                # Check if we have '))'
                if i + 1 < n and s[i + 1] == ')':
                    # Found '))'
                    if open_count > 0:
                        open_count -= 1
                    else:
                        # Need to insert '('
                        insertions += 1
                    i += 2
                else:
                    # Single ')' - need to insert one more ')'
                    insertions += 1
                    if open_count > 0:
                        open_count -= 1
                    else:
                        # Also need to insert '('
                        insertions += 1
                    i += 1

        # Each remaining '(' needs '))'
        insertions += 2 * open_count

        return insertions


class SolutionAlternative:
    def minInsertions(self, s: str) -> int:
        """
        Track needed ')' count instead.
        """
        insertions = 0
        need_close = 0  # Number of ')' needed to balance

        for c in s:
            if c == '(':
                # Each '(' needs 2 ')'
                if need_close % 2 == 1:
                    # Odd number of ')' pending - insert one to pair with previous '('
                    insertions += 1
                    need_close -= 1
                need_close += 2
            else:
                # c == ')'
                if need_close > 0:
                    need_close -= 1
                else:
                    # No '(' to match, insert one
                    insertions += 1
                    need_close += 1  # The inserted '(' still needs one more ')'

        # Remaining ')' needed
        insertions += need_close

        return insertions


class SolutionSimplified:
    def minInsertions(self, s: str) -> int:
        """
        Simplified logic tracking '(' and ')'.
        """
        result = 0
        balance = 0  # Number of ')' needed

        for c in s:
            if c == '(':
                # Handle odd balance before adding new '('
                if balance % 2:
                    result += 1
                    balance -= 1
                balance += 2
            else:
                balance -= 1
                if balance < 0:
                    result += 1
                    balance += 2

        return result + balance


class SolutionStack:
    def minInsertions(self, s: str) -> int:
        """
        Stack-based approach (less efficient but intuitive).
        """
        insertions = 0
        stack = []  # Stack of '('

        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                i += 1
            else:
                # Count consecutive ')'
                close_count = 0
                while i < len(s) and s[i] == ')':
                    close_count += 1
                    i += 1

                # Process pairs of '))'
                while close_count >= 2:
                    if stack:
                        stack.pop()
                    else:
                        insertions += 1
                    close_count -= 2

                # Handle remaining single ')'
                if close_count == 1:
                    if stack:
                        stack.pop()
                        insertions += 1  # Need one more ')'
                    else:
                        insertions += 2  # Need '(' and ')'

        # Each remaining '(' needs '))'
        insertions += 2 * len(stack)

        return insertions
