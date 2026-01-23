#1450. Number of Students Doing Homework at a Given Time
#Easy
#
#Given two integer arrays startTime and endTime and given an integer queryTime.
#
#The ith student started doing their homework at the time startTime[i] and
#finished it at time endTime[i].
#
#Return the number of students doing their homework at time queryTime. More
#formally, return the number of students where queryTime lays in the interval
#[startTime[i], endTime[i]] inclusive.
#
#Example 1:
#Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
#Output: 1
#Explanation: We have 3 students where:
#The first student started doing homework at time 1 and finished at time 3 and
#wasn't doing anything at time 4.
#The second student started doing homework at time 2 and finished at time 2 and
#also wasn't doing anything at time 4.
#The third student started doing homework at time 3 and finished at time 7 and
#was the only student doing homework at time 4.
#
#Example 2:
#Input: startTime = [4], endTime = [4], queryTime = 4
#Output: 1
#Explanation: The only student was doing their homework at the queryTime.
#
#Constraints:
#    startTime.length == endTime.length
#    1 <= startTime.length <= 100
#    1 <= startTime[i] <= endTime[i] <= 1000
#    1 <= queryTime <= 1000

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        Count students where startTime[i] <= queryTime <= endTime[i]
        """
        count = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1
        return count


class SolutionOneLiner:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """Pythonic one-liner"""
        return sum(1 for s, e in zip(startTime, endTime) if s <= queryTime <= e)


class SolutionDifferenceArray:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        Difference array approach (overkill for this problem, but demonstrates technique).
        Mark +1 at start, -1 at end+1, then prefix sum.
        """
        max_time = max(endTime)
        if queryTime > max_time:
            return 0

        diff = [0] * (max_time + 2)

        for s, e in zip(startTime, endTime):
            diff[s] += 1
            diff[e + 1] -= 1

        # Prefix sum up to queryTime
        current = 0
        for t in range(queryTime + 1):
            current += diff[t]

        return current
