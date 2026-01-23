#1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
#Medium
#
#LeetCode company workers use key-cards to unlock office doors. Each time a
#worker uses their key-card, the security system saves the worker's name and
#the time when it was used. The system emits an alert if any worker uses the
#key-card three or more times in a one-hour period.
#
#You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]]
#corresponds to a person's name and the time when their key-card was used in a
#single day.
#
#Access times are given in the 24-hour time format "HH:MM", such as "23:51" and
#"09:49".
#
#Return a list of unique worker names who received an alert for frequent keycard
#use. Sort the names in ascending order alphabetically.
#
#Notice that "10:00" - "11:00" is considered to be within a one-hour period,
#while "22:51" - "23:52" is not considered to be within a one-hour period.
#
#Example 1:
#Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"],
#       keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
#Output: ["daniel"]
#Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
#
#Example 2:
#Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"],
#       keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
#Output: ["bob"]
#Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20","21:30").
#
#Constraints:
#    1 <= keyName.length, keyTime.length <= 10^5
#    keyName.length == keyTime.length
#    keyTime[i] is in the format "HH:MM".
#    [keyName[i], keyTime[i]] is unique.
#    1 <= keyName[i].length <= 10
#    keyName[i] contains only lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        """
        Group times by name, sort, and check for 3 accesses within 1 hour.
        """
        def to_minutes(time: str) -> int:
            h, m = map(int, time.split(':'))
            return h * 60 + m

        # Group times by person
        times_by_name = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            times_by_name[name].append(to_minutes(time))

        alerted = []

        for name, times in times_by_name.items():
            times.sort()

            # Check if any window of size 3 is within 60 minutes
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    alerted.append(name)
                    break

        return sorted(alerted)


class SolutionSlidingWindow:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        """
        Sliding window approach for each person.
        """
        def time_to_min(t: str) -> int:
            return int(t[:2]) * 60 + int(t[3:])

        # Group access times
        accesses = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            accesses[name].append(time_to_min(time))

        result = []

        for name, times in accesses.items():
            times.sort()

            # Sliding window: find 3+ accesses within 60 min
            left = 0
            for right in range(len(times)):
                while times[right] - times[left] > 60:
                    left += 1

                if right - left + 1 >= 3:
                    result.append(name)
                    break

        return sorted(result)


class SolutionDetailed:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        """
        Detailed solution with comments.
        """
        # Convert time string to minutes for easy comparison
        def parse_time(time_str: str) -> int:
            hours, minutes = time_str.split(':')
            return int(hours) * 60 + int(minutes)

        # Build mapping: name -> list of access times (in minutes)
        name_to_times = defaultdict(list)

        for i in range(len(keyName)):
            name = keyName[i]
            time_minutes = parse_time(keyTime[i])
            name_to_times[name].append(time_minutes)

        # Check each person
        alerts = []

        for name, times in name_to_times.items():
            # Sort access times
            times.sort()

            # Check consecutive windows of 3
            triggered = False
            for i in range(len(times) - 2):
                # Check if times[i], times[i+1], times[i+2] are within 1 hour
                if times[i + 2] - times[i] <= 60:
                    triggered = True
                    break

            if triggered:
                alerts.append(name)

        # Return sorted alphabetically
        return sorted(alerts)
