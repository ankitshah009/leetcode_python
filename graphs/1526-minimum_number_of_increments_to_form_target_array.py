#1526. Minimum Number of Increments on Subarrays to Form a Target Array
#Hard
#
#You are given an integer array target. You have an integer array initial of
#the same size as target with all elements initially zeros.
#
#In one operation you can choose any subarray from initial and increment each
#value by one.
#
#Return the minimum number of operations to form a target array from initial.
#
#The test cases are generated so that the answer fits in a 32-bit integer.
#
#Example 1:
#Input: target = [1,2,3,2,1]
#Output: 3
#Explanation: We need at least 3 operations to form the target array from the
#initial array.
#[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
#[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
#[1,2,2,2,1] increment 1 from index 2 to 2 (inclusive).
#[1,2,3,2,1] target array is formed.
#
#Example 2:
#Input: target = [3,1,1,2]
#Output: 4
#Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
#
#Example 3:
#Input: target = [3,1,5,4,2]
#Output: 7
#Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,2,2,2,2] -> [3,2,2,2,2] ->
#[3,1,2,2,2] -> [3,1,5,5,5] -> [3,1,5,4,4] -> [3,1,5,4,2].
#
#Constraints:
#    1 <= target.length <= 10^5
#    1 <= target[i] <= 10^5

from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Key insight: count the number of "ascending steps".
        Each time value increases from previous, we need that many more operations.

        Think of it as painting layers: when we go up, we start new layers.
        When we go down or stay same, existing layers continue.
        """
        operations = target[0]  # Need target[0] operations to get first element

        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                # Need additional operations for the increase
                operations += target[i] - target[i - 1]

        return operations


class SolutionExplained:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Detailed explanation:

        Consider target = [3, 1, 5, 4, 2]

        Visualize as stacks:
        Position:  0  1  2  3  4
                   3  1  5  4  2
                   *     *  *  *
                   *     *  *  *
                   *  *  *  *  *

        Count ascending differences:
        - Start at 0, go to 3: +3 operations
        - 3 to 1: decrease, no new operations (existing ones end)
        - 1 to 5: +4 operations
        - 5 to 4: decrease, no new operations
        - 4 to 2: decrease, no new operations

        Total = 3 + 4 = 7
        """
        result = target[0]

        for i in range(1, len(target)):
            increase = max(0, target[i] - target[i - 1])
            result += increase

        return result


class SolutionRecursive:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Recursive divide and conquer approach (for understanding).
        """
        def helper(arr: List[int], offset: int) -> int:
            if not arr:
                return 0

            min_val = min(arr)

            # Need (min_val - offset) operations to raise entire array to min_val
            ops = min_val - offset

            # Split array at positions where value equals min_val
            # and recursively solve for remaining parts
            segments = []
            current = []

            for x in arr:
                if x > min_val:
                    current.append(x)
                else:
                    if current:
                        segments.append(current)
                        current = []

            if current:
                segments.append(current)

            for seg in segments:
                ops += helper(seg, min_val)

            return ops

        return helper(target, 0)


class SolutionMonotonic:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Using monotonic stack concept.
        """
        result = 0
        prev = 0

        for val in target:
            if val > prev:
                result += val - prev
            prev = val

        return result
