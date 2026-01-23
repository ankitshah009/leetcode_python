#946. Validate Stack Sequences
#Medium
#
#Given two integer arrays pushed and popped each with distinct values, return
#true if this could have been the result of a sequence of push and pop
#operations on an initially empty stack, or false otherwise.
#
#Example 1:
#Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
#Output: true
#Explanation: Push 1,2,3,4; pop 4; push 5; pop 5,3,2,1.
#
#Example 2:
#Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
#Output: false
#Explanation: 1 cannot be popped before 2.
#
#Constraints:
#    1 <= pushed.length <= 1000
#    0 <= pushed[i] <= 1000
#    All the elements of pushed are unique.
#    popped.length == pushed.length
#    popped is a permutation of pushed.

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Simulate stack operations.
        """
        stack = []
        pop_idx = 0

        for val in pushed:
            stack.append(val)

            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

        return len(stack) == 0


class SolutionExplicit:
    """More explicit simulation"""

    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        push_idx = 0
        pop_idx = 0
        n = len(pushed)

        while pop_idx < n:
            # If stack top matches, pop
            if stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
            # Otherwise, push next element
            elif push_idx < n:
                stack.append(pushed[push_idx])
                push_idx += 1
            else:
                # Nothing more to push and can't pop
                return False

        return True


class SolutionInPlace:
    """Use pushed array as stack (in-place)"""

    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack_top = -1  # Index of stack top in pushed array
        pop_idx = 0

        for val in pushed:
            stack_top += 1
            pushed[stack_top] = val

            while stack_top >= 0 and pushed[stack_top] == popped[pop_idx]:
                stack_top -= 1
                pop_idx += 1

        return stack_top == -1
