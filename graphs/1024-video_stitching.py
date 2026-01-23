#1024. Video Stitching
#Medium
#
#You are given a series of video clips from a sporting event that lasted time
#seconds. These video clips can be overlapping with each other and have varying
#lengths.
#
#Each video clip is described by an array clips where clips[i] = [starti, endi]
#indicates that the ith clip started at starti and ended at endi.
#
#We can cut these clips into segments freely.
#
#Return the minimum number of clips needed so that we can cut the clips into
#segments that cover the entire sporting event [0, time]. If the task is
#impossible, return -1.
#
#Example 1:
#Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
#Output: 3
#Explanation: We take clips [0,2], [1,9], and [8,10].
#
#Example 2:
#Input: clips = [[0,1],[1,2]], time = 5
#Output: -1
#
#Example 3:
#Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],
#               [2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
#Output: 3
#
#Constraints:
#    1 <= clips.length <= 100
#    0 <= starti <= endi <= 100
#    1 <= time <= 100

from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
        Greedy: At each position, extend as far as possible.
        Sort clips by start time, track farthest reachable.
        """
        clips.sort()
        count = 0
        current_end = 0
        farthest = 0
        i = 0

        while current_end < time:
            # Find clip starting at or before current_end with farthest reach
            while i < len(clips) and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1

            if farthest == current_end:
                return -1  # Can't extend further

            count += 1
            current_end = farthest

        return count


class SolutionDP:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
        DP: dp[i] = minimum clips to cover [0, i]
        """
        INF = float('inf')
        dp = [INF] * (time + 1)
        dp[0] = 0

        for t in range(1, time + 1):
            for start, end in clips:
                if start < t <= end:
                    dp[t] = min(dp[t], dp[start] + 1)

        return dp[time] if dp[time] != INF else -1


class SolutionJumpGame:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
        Transform to jump game: farthest[i] = max reach from position i
        """
        farthest = [0] * (time + 1)
        for start, end in clips:
            if start <= time:
                farthest[start] = max(farthest[start], end)

        count = 0
        current_end = 0
        next_end = 0

        for i in range(time):
            next_end = max(next_end, farthest[i])
            if i == current_end:
                if next_end == current_end:
                    return -1
                count += 1
                current_end = next_end

        return count
