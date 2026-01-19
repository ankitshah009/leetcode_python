#301. Remove Invalid Parentheses
#Hard
#
#Given a string s that contains parentheses and letters, remove the minimum
#number of invalid parentheses to make the input string valid.
#
#Return a list of unique strings that are valid with the minimum number of
#removals. You may return the answer in any order.
#
#Example 1:
#Input: s = "()())()"
#Output: ["(())()","()()()"]
#
#Example 2:
#Input: s = "(a)())()"
#Output: ["(a())()","(a)()()"]
#
#Example 3:
#Input: s = ")("
#Output: [""]
#
#Constraints:
#    1 <= s.length <= 25
#    s consists of lowercase English letters and parentheses '(' and ')'.
#    There will be at most 20 parentheses in s.

from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """BFS approach - find all strings with minimum removals"""

        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        result = []
        visited = {s}
        queue = deque([s])
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue  # Don't generate shorter strings once we found valid ones

            # Generate all strings with one character removed
            for i in range(len(current)):
                if current[i] in '()':
                    new_string = current[:i] + current[i+1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

        return result if result else [""]


class SolutionDFS:
    """DFS with pruning"""

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Count minimum removals needed
        def count_removals(s):
            left = right = 0
            for char in s:
                if char == '(':
                    left += 1
                elif char == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left, right

        left_rem, right_rem = count_removals(s)
        result = set()

        def dfs(index, left, right, open_count, path):
            if left < 0 or right < 0 or open_count < 0:
                return

            if index == len(s):
                if left == 0 and right == 0 and open_count == 0:
                    result.add(path)
                return

            char = s[index]

            if char == '(':
                # Remove this '('
                dfs(index + 1, left - 1, right, open_count, path)
                # Keep this '('
                dfs(index + 1, left, right, open_count + 1, path + char)

            elif char == ')':
                # Remove this ')'
                dfs(index + 1, left, right - 1, open_count, path)
                # Keep this ')'
                dfs(index + 1, left, right, open_count - 1, path + char)

            else:
                # Regular character, keep it
                dfs(index + 1, left, right, open_count, path + char)

        dfs(0, left_rem, right_rem, 0, "")

        return list(result) if result else [""]
