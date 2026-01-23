#1870. Minimum Speed to Arrive on Time
#Medium
#
#You are given a floating-point number hour, representing the amount of time
#you have to reach the office. To commute to the office, you must take n trains
#in sequential order. You are also given an integer array dist of length n,
#where dist[i] describes the distance (in kilometers) of the ith train ride.
#
#Each train can only depart at an integer hour, so you may need to wait in
#between each train ride.
#
#For example, if the 1st train ride takes 1.5 hours, you must wait for an
#additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour
#mark.
#
#Return the minimum positive integer speed (in kilometers per hour) that all
#the trains must travel at for you to reach the office on time, or -1 if it is
#impossible to be on time.
#
#Tests are generated such that the answer will not exceed 10^7 and hour will
#have at most two decimal places.
#
#Example 1:
#Input: dist = [1,3,2], hour = 6
#Output: 1
#
#Example 2:
#Input: dist = [1,3,2], hour = 2.7
#Output: 3
#
#Example 3:
#Input: dist = [1,3,2], hour = 1.9
#Output: -1
#
#Constraints:
#    n == dist.length
#    1 <= n <= 10^5
#    1 <= dist[i] <= 10^5
#    1 <= hour <= 10^9
#    There will be at most two digits after the decimal point in hour.

from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """
        Binary search on speed.
        """
        n = len(dist)

        # Need at least n-1 hours for n trains (each waits except last)
        if hour <= n - 1:
            return -1

        def can_arrive(speed: int) -> bool:
            """Check if we can arrive on time with given speed."""
            total_time = 0.0
            for i in range(n - 1):
                # Ceil for all but last train (must wait for next hour)
                total_time += math.ceil(dist[i] / speed)
            # Last train doesn't need to wait
            total_time += dist[-1] / speed
            return total_time <= hour

        left, right = 1, 10**7

        while left < right:
            mid = (left + right) // 2
            if can_arrive(mid):
                right = mid
            else:
                left = mid + 1

        return left if can_arrive(left) else -1


class SolutionOptimized:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """
        Optimized with better bounds.
        """
        n = len(dist)

        if hour <= n - 1:
            return -1

        def time_needed(speed: int) -> float:
            total = 0
            for i in range(n - 1):
                total += (dist[i] + speed - 1) // speed  # Ceiling division
            total += dist[-1] / speed
            return total

        # Lower bound: if no waiting, total_dist / hour
        # Upper bound: max_dist / 0.01 (for last train in 0.01 hours)
        lo, hi = 1, 10**7

        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if time_needed(mid) <= hour:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return result
