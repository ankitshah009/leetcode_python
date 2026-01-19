#301. Remove Invalid Parentheses
#Hard
#
#Given a string s that contains parentheses and letters, remove the minimum number of invalid
#parentheses to make the input string valid.
#
#Return a list of unique strings that are valid with the minimum number of removals.
#You may return the answer in any order.
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

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
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

        # BFS to find minimum removals
        result = []
        visited = {s}
        queue = [s]
        found = False

        while queue and not found:
            next_queue = []
            for string in queue:
                if is_valid(string):
                    result.append(string)
                    found = True

                if not found:
                    for i in range(len(string)):
                        if string[i] in '()':
                            new_string = string[:i] + string[i+1:]
                            if new_string not in visited:
                                visited.add(new_string)
                                next_queue.append(new_string)

            queue = next_queue

        return result if result else [""]
