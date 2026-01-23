#754. Reach a Number
#Medium
#
#You are standing at position 0 on an infinite number line. There is a
#destination at position target.
#
#You can make some number of moves numMoves so that:
#- On the ith move, you take i steps forward or backward.
#- More formally, you can take step = i or step = -i.
#
#Given the integer target, return the minimum number of moves required to reach
#the destination.
#
#Example 1:
#Input: target = 2
#Output: 3
#Explanation:
#On the 1st move, we step from 0 to 1 (1 step).
#On the 2nd move, we step from 1 to -1 (2 steps).
#On the 3rd move, we step from -1 to 2 (3 steps).
#
#Example 2:
#Input: target = 3
#Output: 2
#Explanation:
#On the 1st move, we step from 0 to 1 (1 step).
#On the 2nd move, we step from 1 to 3 (2 steps).
#
#Constraints:
#    -10^9 <= target <= 10^9

class Solution:
    def reachNumber(self, target: int) -> int:
        """
        Key insight: if sum - target is even, we can flip one step to reach target.
        1+2+...+n - 2*k = target means we flip step k to negative.
        """
        target = abs(target)  # Symmetric, only consider positive

        # Find smallest n where 1+2+...+n >= target
        n = 0
        total = 0

        while total < target:
            n += 1
            total += n

        # If difference is even, we can reach target
        # If difference is odd, we need more steps
        while (total - target) % 2 != 0:
            n += 1
            total += n

        return n


class SolutionMath:
    """Direct mathematical formula"""

    def reachNumber(self, target: int) -> int:
        import math

        target = abs(target)

        # Solve n(n+1)/2 >= target
        # n^2 + n - 2*target >= 0
        # n >= (-1 + sqrt(1 + 8*target)) / 2
        n = math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2)

        total = n * (n + 1) // 2

        while (total - target) % 2 != 0:
            n += 1
            total += n

        return n


class SolutionBFS:
    """BFS approach (for small targets)"""

    def reachNumber(self, target: int) -> int:
        from collections import deque

        target = abs(target)

        if target == 0:
            return 0

        queue = deque([(0, 0)])  # (position, step)
        visited = {0}

        while queue:
            pos, step = queue.popleft()
            step += 1

            for next_pos in (pos + step, pos - step):
                if next_pos == target:
                    return step

                if abs(next_pos) < target + step and next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, step))

        return -1
