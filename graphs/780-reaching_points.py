#780. Reaching Points
#Hard
#
#Given four integers sx, sy, tx, and ty, return true if it is possible to
#convert the point (sx, sy) to the point (tx, ty) through some operations,
#or false otherwise.
#
#The allowed operation on some point (x, y) is to convert it to either
#(x, x + y) or (x + y, y).
#
#Example 1:
#Input: sx = 1, sy = 1, tx = 3, ty = 5
#Output: true
#Explanation: One series of moves that transforms the starting point to the
#target is: (1, 1) -> (1, 2) -> (3, 2) -> (3, 5)
#
#Example 2:
#Input: sx = 1, sy = 1, tx = 2, ty = 2
#Output: false
#
#Example 3:
#Input: sx = 1, sy = 1, tx = 1, ty = 1
#Output: true
#
#Constraints:
#    1 <= sx, sy, tx, ty <= 10^9

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        Work backwards: (tx, ty) -> (tx - ty, ty) or (tx, ty - tx).
        Use modulo for efficiency when one coordinate is much larger.
        """
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True

            if tx > ty:
                # Can only have come from (tx - ty, ty)
                if ty == sy:
                    # Check if we can reach sx from tx by subtracting sy
                    return (tx - sx) % sy == 0
                tx %= ty
            else:
                # Can only have come from (tx, ty - tx)
                if tx == sx:
                    # Check if we can reach sy from ty by subtracting sx
                    return (ty - sy) % sx == 0
                ty %= tx

        return False


class SolutionRecursive:
    """Recursive with memoization (may TLE for large inputs)"""

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def can_reach(x, y):
            if x == tx and y == ty:
                return True
            if x > tx or y > ty:
                return False
            return can_reach(x + y, y) or can_reach(x, x + y)

        return can_reach(sx, sy)


class SolutionDetailed:
    """More explicit backward approach"""

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        if tx == sx and ty == sy:
            return True

        if tx == sx:
            # ty must be reachable from sy by adding sx repeatedly
            return ty > sy and (ty - sy) % sx == 0

        if ty == sy:
            # tx must be reachable from sx by adding sy repeatedly
            return tx > sx and (tx - sx) % sy == 0

        return False
