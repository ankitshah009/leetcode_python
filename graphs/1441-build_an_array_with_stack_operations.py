#1441. Build an Array With Stack Operations
#Medium
#
#You are given an integer array target and an integer n.
#
#You have an empty stack with the two following operations:
#    "Push": pushes an integer to the top of the stack.
#    "Pop": removes the integer on the top of the stack.
#
#You also have a stream of the integers in the range [1, n].
#
#Use the two stack operations to make the numbers in the stack (from the bottom
#to the top) equal to target. You should follow the following rules:
#    If the stream of the integers is not empty, pick the next integer from the
#    stream and push it to the top of the stack.
#    If the stack is not empty, you may pop the integer on the top of the stack.
#    If, at any moment, the elements in the stack (from the bottom to the top)
#    are equal to target, do not read new integers from the stream and do not do
#    more operations on the stack.
#
#Return the stack operations needed to build target following the mentioned rules.
#If there are multiple valid answers, return any of them.
#
#Example 1:
#Input: target = [1,3], n = 3
#Output: ["Push","Push","Pop","Push"]
#Explanation: Initially the stack s is empty.
#Read 1 from the stream and push it to the stack. s = [1].
#Read 2 from the stream and push it to the stack. s = [1,2].
#Pop the integer on the top of the stack. s = [1].
#Read 3 from the stream and push it to the stack. s = [1,3].
#
#Example 2:
#Input: target = [1,2,3], n = 3
#Output: ["Push","Push","Push"]
#Explanation: Initially the stack s is empty.
#Read 1 from the stream and push it to the stack. s = [1].
#Read 2 from the stream and push it to the stack. s = [1,2].
#Read 3 from the stream and push it to the stack. s = [1,2,3].
#
#Example 3:
#Input: target = [1,2], n = 4
#Output: ["Push","Push"]
#Explanation: Initially the stack s is empty.
#Read 1 from the stream and push it to the stack. s = [1].
#Read 2 from the stream and push it to the stack. s = [1,2].
#Since the stack (from the bottom to the top) is equal to target, we stop.
#
#Constraints:
#    1 <= target.length <= 100
#    1 <= n <= 100
#    1 <= target[i] <= n
#    target is strictly increasing.

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        For each number in stream [1, n]:
        - If number is in target: Push
        - If number is not in target but < max(target): Push then Pop
        - Stop when stack equals target
        """
        operations = []
        target_set = set(target)
        target_idx = 0

        for num in range(1, n + 1):
            if target_idx >= len(target):
                break

            if num == target[target_idx]:
                operations.append("Push")
                target_idx += 1
            elif num < target[target_idx]:
                operations.append("Push")
                operations.append("Pop")

        return operations


class SolutionExplicit:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """More explicit version"""
        operations = []
        stream = 1
        idx = 0

        while idx < len(target):
            # Push current stream number
            operations.append("Push")

            if stream == target[idx]:
                # Keep this number
                idx += 1
            else:
                # Not needed, pop it
                operations.append("Pop")

            stream += 1

        return operations


class SolutionSimple:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """Simple iteration through target"""
        ops = []
        prev = 0

        for num in target:
            # Numbers between prev+1 and num-1 need push+pop
            for _ in range(num - prev - 1):
                ops.extend(["Push", "Pop"])
            # num itself needs push
            ops.append("Push")
            prev = num

        return ops
