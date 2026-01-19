#282. Expression Add Operators
#Hard
#
#Given a string num that contains only digits and an integer target, return all
#possibilities to insert the binary operators '+', '-', and/or '*' between the
#digits of num so that the resultant expression evaluates to the target value.
#
#Note that operands in the returned expressions should not contain leading zeros.
#
#Example 1:
#Input: num = "123", target = 6
#Output: ["1*2*3","1+2+3"]
#Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
#
#Example 2:
#Input: num = "232", target = 8
#Output: ["2*3+2","2+3*2"]
#Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
#
#Example 3:
#Input: num = "3456237490", target = 9191
#Output: []
#Explanation: There are no expressions that can be created to evaluate to 9191.
#
#Constraints:
#    1 <= num.length <= 10
#    num consists of only digits.
#    -2^31 <= target <= 2^31 - 1

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        n = len(num)

        def backtrack(idx, path, value, prev_operand):
            # Base case: reached end of string
            if idx == n:
                if value == target:
                    result.append(path)
                return

            for i in range(idx, n):
                # Extract substring
                substr = num[idx:i+1]

                # Skip numbers with leading zeros (except "0" itself)
                if len(substr) > 1 and substr[0] == '0':
                    break

                curr = int(substr)

                if idx == 0:
                    # First number, no operator before it
                    backtrack(i + 1, substr, curr, curr)
                else:
                    # Try addition
                    backtrack(i + 1, path + '+' + substr, value + curr, curr)

                    # Try subtraction
                    backtrack(i + 1, path + '-' + substr, value - curr, -curr)

                    # Try multiplication
                    # Need to handle operator precedence: undo prev, apply mult
                    backtrack(i + 1, path + '*' + substr,
                             value - prev_operand + prev_operand * curr,
                             prev_operand * curr)

        backtrack(0, "", 0, 0)
        return result
