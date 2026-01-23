#755. Pour Water
#Medium
#
#You are given an elevation map represents as an integer array heights where
#heights[i] representing the height of the terrain at index i. The width at
#each index is 1. You are also given two integers volume and k. volume units
#of water will fall at index k.
#
#Water first drops at the index k and rests on top of the highest terrain or
#water at that index. Then, it flows according to the following rules:
#
#1. If the droplet would eventually fall by moving left, then move left.
#2. Otherwise, if the droplet would eventually fall by moving right, then move
#   right.
#3. Otherwise, rise to it's current position.
#
#Here, "eventually fall" means that the droplet will eventually be at a lower
#level if it moves in that direction. Also, level means the height of the
#terrain plus any water in that column.
#
#Return the final state of heights after pouring volume units of water.
#
#Example 1:
#Input: heights = [2,1,1,2,1,2,2], volume = 4, k = 3
#Output: [2,2,2,3,2,2,2]
#
#Example 2:
#Input: heights = [1,2,3,4], volume = 2, k = 2
#Output: [2,3,3,4]
#
#Constraints:
#    1 <= heights.length <= 100
#    0 <= heights[i] <= 99
#    0 <= volume <= 2000
#    0 <= k < heights.length

class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        """
        Simulate each water droplet falling.
        """
        n = len(heights)

        for _ in range(volume):
            # Try moving left
            best = k
            i = k - 1

            while i >= 0 and heights[i] <= heights[i + 1]:
                if heights[i] < heights[best]:
                    best = i
                i -= 1

            if best != k:
                heights[best] += 1
                continue

            # Try moving right
            best = k
            i = k + 1

            while i < n and heights[i] <= heights[i - 1]:
                if heights[i] < heights[best]:
                    best = i
                i += 1

            if best != k:
                heights[best] += 1
                continue

            # Stay at k
            heights[k] += 1

        return heights


class SolutionOptimized:
    """Optimized to find lowest point faster"""

    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        n = len(heights)

        for _ in range(volume):
            drop_idx = k

            # Check left
            i = k
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
                if heights[i] < heights[drop_idx]:
                    drop_idx = i

            # If no left drop point found, check right
            if drop_idx == k:
                i = k
                while i < n - 1 and heights[i + 1] <= heights[i]:
                    i += 1
                    if heights[i] < heights[drop_idx]:
                        drop_idx = i

            heights[drop_idx] += 1

        return heights


class SolutionVisual:
    """With visualization helper"""

    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        n = len(heights)
        water = [0] * n  # Track water separately

        for _ in range(volume):
            level = heights[:]
            for i in range(n):
                level[i] += water[i]

            # Find drop position
            drop = k

            # Try left
            for i in range(k - 1, -1, -1):
                if level[i] > level[i + 1]:
                    break
                if level[i] < level[drop]:
                    drop = i

            # Try right if left didn't work
            if drop == k:
                for i in range(k + 1, n):
                    if level[i] > level[i - 1]:
                        break
                    if level[i] < level[drop]:
                        drop = i

            water[drop] += 1

        return [heights[i] + water[i] for i in range(n)]
