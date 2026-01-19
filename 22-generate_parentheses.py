#22. Generate Parentheses
#Medium
#
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#Example 1:
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#
#Example 2:
#Input: n = 1
#Output: ["()"]
#
#Constraints:
#    1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
