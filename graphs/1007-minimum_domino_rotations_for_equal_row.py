#1007. Minimum Domino Rotations For Equal Row
#Medium
#
#In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom
#halves of the i-th domino.
#
#We may rotate the i-th domino, so that tops[i] and bottoms[i] swap values.
#
#Return the minimum number of rotations so that all the values in tops are the
#same, or all the values in bottoms are the same. If it cannot be done, return -1.
#
#Example 1:
#Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
#Output: 2
#Explanation: Rotate at indices 1 and 3.
#
#Example 2:
#Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
#Output: -1
#
#Constraints:
#    2 <= tops.length <= 2 * 10^4
#    bottoms.length == tops.length
#    1 <= tops[i], bottoms[i] <= 6

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        """
        Only tops[0] or bottoms[0] can be the target value.
        """
        def rotations(target):
            top_rotations = 0
            bottom_rotations = 0

            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return float('inf')
                if t != target:
                    top_rotations += 1
                if b != target:
                    bottom_rotations += 1

            return min(top_rotations, bottom_rotations)

        result = min(rotations(tops[0]), rotations(bottoms[0]))
        return result if result != float('inf') else -1


class SolutionCount:
    """Counting approach"""

    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target):
            top_rot = bottom_rot = 0

            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                elif tops[i] != target:
                    top_rot += 1
                elif bottoms[i] != target:
                    bottom_rot += 1

            return min(top_rot, bottom_rot)

        result = check(tops[0])
        if result != -1:
            return result

        if tops[0] != bottoms[0]:
            result = check(bottoms[0])
            if result != -1:
                return result

        return -1


class SolutionSet:
    """Set intersection"""

    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        # Find values that appear in every domino
        candidates = set(range(1, 7))

        for t, b in zip(tops, bottoms):
            candidates &= {t, b}

        if not candidates:
            return -1

        target = candidates.pop()
        top_rot = sum(t != target for t in tops)
        bottom_rot = sum(b != target for b in bottoms)

        return min(top_rot, bottom_rot)
