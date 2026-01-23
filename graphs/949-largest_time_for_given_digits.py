#949. Largest Time for Given Digits
#Medium
#
#Given an array arr of 4 digits, find the latest 24-hour time that can be made
#using each digit exactly once.
#
#24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM
#is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is
#23:59.
#
#Return the latest 24-hour time in "HH:MM" format. If no valid time can be made,
#return an empty string.
#
#Example 1:
#Input: arr = [1,2,3,4]
#Output: "23:41"
#
#Example 2:
#Input: arr = [5,5,5,5]
#Output: ""
#
#Example 3:
#Input: arr = [0,0,0,0]
#Output: "00:00"
#
#Constraints:
#    arr.length == 4
#    0 <= arr[i] <= 9

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        """
        Try all permutations, find max valid time.
        """
        max_time = -1

        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2

            if hour < 24 and minute < 60:
                time = hour * 60 + minute
                max_time = max(max_time, time)

        if max_time == -1:
            return ""

        return f"{max_time // 60:02d}:{max_time % 60:02d}"


class SolutionBacktrack:
    """Backtracking approach"""

    def largestTimeFromDigits(self, arr: list[int]) -> str:
        max_time = -1

        def backtrack(idx, used, current):
            nonlocal max_time

            if idx == 4:
                hour = current[0] * 10 + current[1]
                minute = current[2] * 10 + current[3]

                if hour < 24 and minute < 60:
                    max_time = max(max_time, hour * 60 + minute)
                return

            for i in range(4):
                if not used[i]:
                    used[i] = True
                    current.append(arr[i])
                    backtrack(idx + 1, used, current)
                    current.pop()
                    used[i] = False

        backtrack(0, [False] * 4, [])

        if max_time == -1:
            return ""

        return f"{max_time // 60:02d}:{max_time % 60:02d}"


class SolutionGreedy:
    """Greedy digit by digit"""

    def largestTimeFromDigits(self, arr: list[int]) -> str:
        from itertools import permutations

        result = ""

        for p in permutations(arr):
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]

            if hour < 24 and minute < 60:
                time_str = f"{hour:02d}:{minute:02d}"
                if time_str > result:
                    result = time_str

        return result
