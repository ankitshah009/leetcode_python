#1769. Minimum Number of Operations to Move All Balls to Each Box
#Medium
#
#You have n boxes. You are given a binary string boxes of length n, where
#boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
#
#In one operation, you can move one ball from a box to an adjacent box. Box i is
#adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be
#more than one ball in some boxes.
#
#Return an array answer of size n, where answer[i] is the minimum number of
#operations needed to move all the balls to the ith box.
#
#Example 1:
#Input: boxes = "110"
#Output: [1,1,3]
#
#Example 2:
#Input: boxes = "001011"
#Output: [11,8,5,4,3,4]
#
#Constraints:
#    n == boxes.length
#    1 <= n <= 2000
#    boxes[i] is either '0' or '1'.

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Two pass approach - O(n) time, O(1) extra space.
        """
        n = len(boxes)
        result = [0] * n

        # Left to right pass
        balls = 0
        ops = 0
        for i in range(n):
            result[i] += ops
            balls += int(boxes[i])
            ops += balls

        # Right to left pass
        balls = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            result[i] += ops
            balls += int(boxes[i])
            ops += balls

        return result


class SolutionBruteForce:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Brute force - O(n^2).
        """
        n = len(boxes)
        result = []

        for i in range(n):
            ops = sum(abs(i - j) for j in range(n) if boxes[j] == '1')
            result.append(ops)

        return result


class SolutionPrefixSum:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Using prefix sums.
        """
        n = len(boxes)

        # Find ball positions
        balls = [i for i in range(n) if boxes[i] == '1']

        if not balls:
            return [0] * n

        # Prefix sum of positions
        prefix = [0]
        for pos in balls:
            prefix.append(prefix[-1] + pos)

        result = []
        for i in range(n):
            # Binary search for split point
            import bisect
            k = bisect.bisect_left(balls, i)

            # Cost from left balls
            left_cost = k * i - prefix[k]

            # Cost from right balls
            right_cost = (prefix[len(balls)] - prefix[k]) - (len(balls) - k) * i

            result.append(left_cost + right_cost)

        return result
