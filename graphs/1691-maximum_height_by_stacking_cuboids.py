#1691. Maximum Height by Stacking Cuboids
#Hard
#
#Given n cuboids where the dimensions of the ith cuboid is
#cuboids[i] = [width_i, length_i, height_i] (0-indexed).
#
#Choose a subset of cuboids and place them on each other.
#
#You can place cuboid i on cuboid j if width_i <= width_j and length_i <= length_j
#and height_i <= height_j. You can rearrange any cuboid's dimensions by rotating
#it to put it on another cuboid.
#
#Return the maximum height of the stacked cuboids.
#
#Example 1:
#Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
#Output: 190
#Explanation: Cuboid 1 placed on cuboid 0, cuboid 2 placed on cuboid 1.
#After rearranging: [20,45,50], [37,53,95], [12,23,45]. Heights: 50+95+45 = 190.
#
#Example 2:
#Input: cuboids = [[38,25,45],[76,35,3]]
#Output: 76
#
#Example 3:
#Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
#Output: 102
#
#Constraints:
#    n == cuboids.length
#    1 <= n <= 100
#    1 <= width_i, length_i, height_i <= 100

from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        """
        Key insight: For maximum height, always orient each cuboid with
        largest dimension as height.

        Then sort and use LIS-like DP.
        """
        # Sort each cuboid dimensions (smallest to largest)
        for c in cuboids:
            c.sort()

        # Sort cuboids by all dimensions
        cuboids.sort()

        n = len(cuboids)
        # dp[i] = max height ending with cuboid i
        dp = [c[2] for c in cuboids]  # Initialize with own height

        for i in range(1, n):
            for j in range(i):
                # Can stack cuboid i on cuboid j?
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        return max(dp)


class SolutionProof:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        """
        Proof that sorting dimensions works:

        If we place cuboid A on cuboid B, we need all dimensions of A <= B.
        To maximize height, we want the height (which we add) to be maximal.
        But we also need width, length <= those of B.

        Claim: Optimal solution exists where each cuboid has dimensions sorted.

        Proof: If A is on B with A.height > A.width, and B.height > B.width,
        we can rotate both to make height the largest dimension without
        violating the stacking constraint.
        """
        # Sort dimensions of each cuboid
        sorted_cuboids = [sorted(c) for c in cuboids]

        # Sort cuboids
        sorted_cuboids.sort()

        n = len(sorted_cuboids)
        dp = [0] * n

        for i in range(n):
            dp[i] = sorted_cuboids[i][2]  # Height of current cuboid

            for j in range(i):
                if all(sorted_cuboids[j][k] <= sorted_cuboids[i][k] for k in range(3)):
                    dp[i] = max(dp[i], dp[j] + sorted_cuboids[i][2])

        return max(dp)


class SolutionAllOrientations:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        """
        Consider all possible orientations (for understanding, not optimal).
        """
        # Generate all orientations for each cuboid
        orientations = []
        for i, (a, b, c) in enumerate(cuboids):
            dims = sorted([a, b, c])
            # Only need the sorted orientation for optimal solution
            orientations.append(dims)

        # Sort by all dimensions
        orientations.sort()

        n = len(orientations)
        dp = [o[2] for o in orientations]

        for i in range(n):
            for j in range(i):
                if (orientations[j][0] <= orientations[i][0] and
                    orientations[j][1] <= orientations[i][1] and
                    orientations[j][2] <= orientations[i][2]):
                    dp[i] = max(dp[i], dp[j] + orientations[i][2])

        return max(dp)


class SolutionCompact:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        """
        Compact solution.
        """
        c = [sorted(x) for x in cuboids]
        c.sort()
        n = len(c)
        dp = [x[2] for x in c]

        for i in range(n):
            for j in range(i):
                if all(c[j][k] <= c[i][k] for k in range(3)):
                    dp[i] = max(dp[i], dp[j] + c[i][2])

        return max(dp)
