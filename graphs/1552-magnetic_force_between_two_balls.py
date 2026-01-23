#1552. Magnetic Force Between Two Balls
#Medium
#
#In the universe Earth C-137, Rick discovered a special form of magnetic force
#between two balls if they are put in his new invented basket. Rick has n empty
#baskets, the ith basket is at position[i], Rick has m balls and needs to
#distribute the balls into the baskets such that the minimum magnetic force
#between any two balls is maximum.
#
#Rick stated that magnetic force between two different balls at positions x and
#y is |x - y|.
#
#Given the integer array position and the integer m. Return the required maximum
#minimum magnetic force.
#
#Example 1:
#Input: position = [1,2,3,4,7], m = 3
#Output: 3
#Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the
#magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3.
#We cannot achieve a larger minimum magnetic force than 3.
#
#Example 2:
#Input: position = [5,4,3,2,1,1000000000], m = 2
#Output: 999999999
#Explanation: We can use baskets 1 and 1000000000.
#
#Constraints:
#    n == position.length
#    2 <= n <= 10^5
#    1 <= position[i] <= 10^9
#    All integers in position are distinct.
#    2 <= m <= position.length

from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Binary search on the answer (minimum distance).

        For a given minimum distance d, check if we can place m balls
        such that each pair is at least d apart.

        Greedy placement: always place ball at earliest possible position.
        """
        position.sort()

        def can_place(min_dist: int) -> bool:
            """Check if we can place m balls with at least min_dist between each."""
            count = 1
            last_pos = position[0]

            for i in range(1, len(position)):
                if position[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = position[i]
                    if count >= m:
                        return True

            return count >= m

        # Binary search for maximum minimum distance
        left = 1
        right = (position[-1] - position[0]) // (m - 1)

        while left < right:
            mid = (left + right + 1) // 2
            if can_place(mid):
                left = mid
            else:
                right = mid - 1

        return left


class SolutionBisect:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Using bisect for binary search.
        """
        import bisect

        position.sort()
        n = len(position)

        def can_place(min_dist: int) -> bool:
            count = 1
            last = position[0]

            for i in range(1, n):
                if position[i] - last >= min_dist:
                    count += 1
                    last = position[i]

            return count >= m

        lo, hi = 1, (position[-1] - position[0]) // (m - 1) + 1

        while lo < hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1


class SolutionDetailed:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Detailed solution with explanation.

        Key insight: This is a classic binary search on answer problem.

        The answer (max min distance) is monotonic:
        - If we can place m balls with min distance d, we can also do it with d-1.
        - If we can't place m balls with min distance d, we can't do it with d+1.

        This monotonicity allows binary search.
        """
        position.sort()

        def feasible(min_force: int) -> bool:
            """
            Greedy check: Can we place m balls with min_force between each pair?

            Strategy: Place first ball at position[0].
            For each subsequent ball, place at the earliest position that's
            at least min_force away from the last placed ball.
            """
            balls_placed = 1
            last_position = position[0]

            for pos in position[1:]:
                if pos - last_position >= min_force:
                    balls_placed += 1
                    last_position = pos

                    if balls_placed == m:
                        return True

            return False

        # Binary search bounds
        lo = 1
        hi = (position[-1] - position[0]) // (m - 1)

        # Find maximum feasible min_force
        result = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return result


class SolutionAlternative:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Alternative binary search template.
        """
        position.sort()

        def count_balls(min_dist: int) -> int:
            """Count max balls we can place with given min distance."""
            count = 1
            prev = position[0]

            for p in position:
                if p - prev >= min_dist:
                    count += 1
                    prev = p

            return count

        left, right = 1, position[-1] - position[0]

        while left < right:
            mid = right - (right - left) // 2
            if count_balls(mid) >= m:
                left = mid
            else:
                right = mid - 1

        return left
