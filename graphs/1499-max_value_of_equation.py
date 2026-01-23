#1499. Max Value of Equation
#Hard
#
#You are given an array points containing the coordinates of points on a 2D
#plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj
#for all 1 <= i < j <= points.length. You are also given an integer k.
#
#Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k
#and 1 <= i < j <= points.length.
#
#It is guaranteed that there exists at least one pair of points that satisfy
#the constraint |xi - xj| <= k.
#
#Example 1:
#Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
#Output: 4
#Explanation: The first two points satisfy the condition |xi - xj| <= k and if
#we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points
#also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
#No other pairs satisfy the condition, so we return max(4, 1) = 4.
#
#Example 2:
#Input: points = [[0,0],[3,0],[9,2]], k = 3
#Output: 3
#Explanation: Only the first two points have an absolute difference of 3 or
#less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
#
#Constraints:
#    2 <= points.length <= 10^5
#    points[i].length == 2
#    -10^8 <= xi, yi <= 10^8
#    0 <= k <= 2 * 10^8
#    points is sorted by xi in strictly increasing order.

from typing import List
from collections import deque
import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        yi + yj + |xi - xj| = yi + yj + xj - xi (since xj > xi)
                            = (yj + xj) + (yi - xi)

        For each j, we want max(yi - xi) among valid i's.
        Use monotonic deque to track (yi - xi, xi) for valid i's.
        """
        # Monotonic deque: stores (yi - xi, xi) in decreasing order of (yi - xi)
        dq = deque()
        result = float('-inf')

        for xj, yj in points:
            # Remove points too far away
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            # Calculate answer using front of deque
            if dq:
                result = max(result, yj + xj + dq[0][0])

            # Add current point, maintaining decreasing order
            val = yj - xj
            while dq and dq[-1][0] <= val:
                dq.pop()
            dq.append((val, xj))

        return result


class SolutionHeap:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        Use max heap to track (yi - xi, xi).
        Max heap gives us the best candidate quickly.
        """
        # Max heap: (-( yi - xi), xi) - negative because Python has min heap
        heap = []
        result = float('-inf')

        for xj, yj in points:
            # Remove invalid points (too far)
            while heap and xj - heap[0][1] > k:
                heapq.heappop(heap)

            # Get answer from top of heap
            if heap:
                result = max(result, yj + xj - heap[0][0])

            # Add current point
            heapq.heappush(heap, (-(yj - xj), xj))

        return result


class SolutionBruteForce:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        Brute force O(n^2) - for comparison only.
        """
        n = len(points)
        result = float('-inf')

        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]

                if xj - xi > k:
                    break  # Points are sorted, no need to check further

                value = yi + yj + xj - xi
                result = max(result, value)

        return result


class SolutionSegmentTree:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        Using coordinate compression and segment tree.
        More complex but demonstrates different approach.
        """
        from collections import deque

        # Use monotonic deque (simpler and same complexity)
        dq = deque()  # (y - x, x)
        result = float('-inf')

        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()

            if dq:
                result = max(result, y + x + dq[0][0])

            while dq and dq[-1][0] <= y - x:
                dq.pop()

            dq.append((y - x, x))

        return result
