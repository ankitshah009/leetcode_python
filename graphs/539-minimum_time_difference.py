#539. Minimum Time Difference
#Medium
#
#Given a list of 24-hour clock time points in "HH:MM" format, return the minimum
#minutes difference between any two time-points in the list.
#
#Example 1:
#Input: timePoints = ["23:59","00:00"]
#Output: 1
#
#Example 2:
#Input: timePoints = ["00:00","23:59","00:00"]
#Output: 0
#
#Constraints:
#    2 <= timePoints.length <= 2 * 10^4
#    timePoints[i] is in the format "HH:MM".

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """Convert to minutes, sort, find min adjacent difference"""
        def to_minutes(time):
            h, m = map(int, time.split(':'))
            return h * 60 + m

        minutes = sorted(to_minutes(t) for t in timePoints)

        # Check consecutive differences
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        # Check wrap-around (last to first across midnight)
        wrap_around = 1440 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, wrap_around)

        return min_diff


class SolutionBucket:
    """Bucket sort approach - O(1) for fixed time range"""

    def findMinDifference(self, timePoints: List[str]) -> int:
        # If more than 1440 time points, there must be duplicates
        if len(timePoints) > 1440:
            return 0

        seen = [False] * 1440

        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes = h * 60 + m
            if seen[minutes]:
                return 0
            seen[minutes] = True

        # Find minimum difference
        first = prev = -1
        min_diff = float('inf')

        for i in range(1440):
            if seen[i]:
                if prev >= 0:
                    min_diff = min(min_diff, i - prev)
                if first < 0:
                    first = i
                prev = i

        # Wrap around
        min_diff = min(min_diff, 1440 - prev + first)

        return min_diff


class SolutionSimple:
    """Simple sorting approach"""

    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = time.split(':')
            minutes.append(int(h) * 60 + int(m))

        minutes.sort()

        min_diff = 1440 + minutes[0] - minutes[-1]  # Wrap around

        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
            if min_diff == 0:
                return 0

        return min_diff
