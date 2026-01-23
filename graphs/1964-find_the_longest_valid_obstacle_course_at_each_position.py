#1964. Find the Longest Valid Obstacle Course at Each Position
#Hard
#
#You want to build some obstacle courses. You are given a 0-indexed integer
#array obstacles of length n, where obstacles[i] describes the height of the
#ith obstacle.
#
#For every index i between 0 and n - 1 (inclusive), find the length of the
#longest obstacle course in obstacles such that:
#- You choose any number of obstacles between 0 and i inclusive.
#- You must include the ith obstacle in the course.
#- You must put the chosen obstacles in the same order as they appear in
#  obstacles.
#- Every obstacle (except the first) is taller than or the same height as the
#  obstacle immediately before it.
#
#Return an array ans of length n, where ans[i] is the length of the longest
#obstacle course for index i as described above.
#
#Example 1:
#Input: obstacles = [1,2,3,2]
#Output: [1,2,3,3]
#
#Example 2:
#Input: obstacles = [2,2,1]
#Output: [1,2,1]
#
#Example 3:
#Input: obstacles = [3,1,5,6,4,2]
#Output: [1,1,2,3,2,2]
#
#Constraints:
#    n == obstacles.length
#    1 <= n <= 10^5
#    1 <= obstacles[i] <= 10^7

from typing import List
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        LIS variant using binary search.
        Find longest non-decreasing subsequence ending at each position.
        """
        n = len(obstacles)
        result = [0] * n
        tails = []  # tails[i] = smallest ending value for length i+1

        for i, height in enumerate(obstacles):
            # Find position to insert (first position where tails[pos] > height)
            pos = bisect.bisect_right(tails, height)

            if pos == len(tails):
                tails.append(height)
            else:
                tails[pos] = height

            result[i] = pos + 1

        return result


class SolutionBIT:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        Binary Indexed Tree approach.
        """
        from collections import defaultdict

        # Coordinate compression
        sorted_unique = sorted(set(obstacles))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        m = len(sorted_unique)

        # BIT for range max query
        bit = [0] * (m + 1)

        def update(idx: int, val: int):
            while idx <= m:
                bit[idx] = max(bit[idx], val)
                idx += idx & (-idx)

        def query(idx: int) -> int:
            result = 0
            while idx > 0:
                result = max(result, bit[idx])
                idx -= idx & (-idx)
            return result

        n = len(obstacles)
        result = [0] * n

        for i, height in enumerate(obstacles):
            r = rank[height]
            # Query max length for heights <= height
            length = query(r) + 1
            result[i] = length
            update(r, length)

        return result


class SolutionSegmentTree:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        Segment tree for range max query.
        """
        # Coordinate compression
        sorted_unique = sorted(set(obstacles))
        rank = {v: i for i, v in enumerate(sorted_unique)}
        m = len(sorted_unique)

        # Segment tree
        tree = [0] * (2 * m)

        def update(idx: int, val: int):
            idx += m
            tree[idx] = max(tree[idx], val)
            while idx > 1:
                idx //= 2
                tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])

        def query(l: int, r: int) -> int:
            result = 0
            l += m
            r += m + 1
            while l < r:
                if l & 1:
                    result = max(result, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    result = max(result, tree[r])
                l //= 2
                r //= 2
            return result

        n = len(obstacles)
        result = [0] * n

        for i, height in enumerate(obstacles):
            r = rank[height]
            length = query(0, r) + 1
            result[i] = length
            update(r, length)

        return result
