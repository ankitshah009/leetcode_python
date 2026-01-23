#1824. Minimum Sideway Jumps
#Medium
#
#There is a 3 lane road of length n that consists of n + 1 points labeled from
#0 to n. A frog starts at point 0 in the second lane and wants to jump to point
#n. However, there could be obstacles along the way.
#
#You are given an array obstacles of length n + 1 where each obstacles[i]
#(ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point
#i. If obstacles[i] == 0, there are no obstacles at point i. There will be at
#most one obstacle in the 3 lanes at each point.
#
#The frog can only travel from point i to point i + 1 on the same lane if there
#is no obstacle on the lane at point i + 1. To avoid obstacles, the frog can
#also perform a side jump to jump to another lane (even if they are not
#adjacent) at the same point if there is no obstacle on the new lane.
#
#Return the minimum number of side jumps the frog needs to reach any lane at
#point n starting from lane 2 at point 0.
#
#Example 1:
#Input: obstacles = [0,1,2,3,0]
#Output: 2
#
#Example 2:
#Input: obstacles = [0,1,1,3,3,0]
#Output: 0
#
#Constraints:
#    obstacles.length == n + 1
#    1 <= n <= 5 * 10^5
#    0 <= obstacles[i] <= 3
#    obstacles[0] == obstacles[n] == 0

from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        DP: track minimum jumps to reach each lane.
        """
        INF = float('inf')
        n = len(obstacles) - 1

        # dp[lane] = min jumps to reach current position at this lane (1-indexed)
        dp = [INF, 1, 0, 1]  # Start at lane 2 (middle)

        for i in range(1, n + 1):
            obs = obstacles[i]

            # Mark obstacle lane as unreachable
            if obs:
                dp[obs] = INF

            # Try side jumps to improve
            min_jumps = min(dp[1], dp[2], dp[3])

            for lane in range(1, 4):
                if lane != obs:
                    dp[lane] = min(dp[lane], min_jumps + 1)

        return min(dp[1], dp[2], dp[3])


class SolutionExplained:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        Same approach with clearer structure.
        """
        INF = float('inf')

        # dp[j] = min jumps to be at lane j (1,2,3) at current point
        dp = [INF, 1, 0, 1]

        for obs in obstacles:
            # Block lane with obstacle
            if obs:
                dp[obs] = INF

            # Try jumping to other lanes
            for lane in range(1, 4):
                if lane != obs:
                    for other in range(1, 4):
                        if other != obs and other != lane:
                            dp[lane] = min(dp[lane], dp[other] + 1)

        return min(dp[1:])


class SolutionBFS:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        BFS approach - state is (position, lane).
        """
        from collections import deque

        n = len(obstacles) - 1
        visited = [[False] * 4 for _ in range(n + 1)]

        # (position, lane, jumps)
        queue = deque([(0, 2, 0)])
        visited[0][2] = True

        while queue:
            pos, lane, jumps = queue.popleft()

            if pos == n:
                return jumps

            # Move forward in same lane
            if obstacles[pos + 1] != lane:
                if not visited[pos + 1][lane]:
                    visited[pos + 1][lane] = True
                    queue.appendleft((pos + 1, lane, jumps))

            # Side jump to other lanes
            for new_lane in range(1, 4):
                if new_lane != lane and obstacles[pos] != new_lane:
                    if not visited[pos][new_lane]:
                        visited[pos][new_lane] = True
                        queue.append((pos, new_lane, jumps + 1))

        return -1
