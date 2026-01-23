#682. Baseball Game
#Easy
#
#You are keeping the scores for a baseball game with strange rules. At the
#beginning of the game, you start with an empty record.
#
#You are given a list of strings operations, where operations[i] is the ith
#operation you must apply to the record and is one of the following:
#- An integer x: Record a new score of x.
#- '+': Record a new score that is the sum of the previous two scores.
#- 'D': Record a new score that is double of the previous score.
#- 'C': Invalidate the previous score, removing it from the record.
#
#Return the sum of all the scores on the record after applying all operations.
#
#Example 1:
#Input: ops = ["5","2","C","D","+"]
#Output: 30
#Explanation:
#"5" - Add 5 to the record, record is now [5].
#"2" - Add 2 to the record, record is now [5, 2].
#"C" - Invalidate and remove the previous score, record is now [5].
#"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
#"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
#The total sum is 5 + 10 + 15 = 30.
#
#Example 2:
#Input: ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27
#
#Constraints:
#    1 <= operations.length <= 1000
#    operations[i] is "C", "D", "+", or a string representing an integer

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Use a stack to track valid scores.
        """
        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


class SolutionVerbose:
    """More explicit version with match-case"""

    def calPoints(self, operations: list[str]) -> int:
        record = []

        for op in operations:
            match op:
                case '+':
                    record.append(record[-1] + record[-2])
                case 'D':
                    record.append(record[-1] * 2)
                case 'C':
                    record.pop()
                case _:
                    record.append(int(op))

        return sum(record)
