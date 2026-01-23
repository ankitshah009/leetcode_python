#681. Next Closest Time
#Medium
#
#Given a time represented in the format "HH:MM", form the next closest time by
#reusing the current digits. There is no limit on how many times a digit can be
#reused.
#
#You may assume the given input string is always valid.
#
#Example 1:
#Input: time = "19:34"
#Output: "19:39"
#Explanation: The next closest time choosing from digits 1, 9, 3, 4 is 19:39.
#
#Example 2:
#Input: time = "23:59"
#Output: "22:22"
#Explanation: The next closest time is 22:22, which is the next day.
#
#Constraints:
#    time.length == 5
#    time is a valid time in the form "HH:MM"
#    0 <= HH < 24
#    0 <= MM < 60

class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
        Generate all valid times using available digits, find the next one.
        """
        digits = set(time.replace(":", ""))

        # Convert current time to minutes
        cur_minutes = int(time[:2]) * 60 + int(time[3:])

        # Try next minute until we find valid time
        for i in range(1, 24 * 60 + 1):
            next_minutes = (cur_minutes + i) % (24 * 60)
            hours, mins = divmod(next_minutes, 60)
            result = f"{hours:02d}:{mins:02d}"

            if all(c in digits or c == ':' for c in result):
                return result

        return time


class SolutionBruteForce:
    """Generate all valid times and find minimum distance"""

    def nextClosestTime(self, time: str) -> str:
        digits = list(set(time.replace(":", "")))
        cur_minutes = int(time[:2]) * 60 + int(time[3:])

        min_diff = float('inf')
        result = time

        # Generate all combinations
        for d1 in digits:
            for d2 in digits:
                hours = int(d1 + d2)
                if hours >= 24:
                    continue
                for d3 in digits:
                    for d4 in digits:
                        mins = int(d3 + d4)
                        if mins >= 60:
                            continue

                        candidate_minutes = hours * 60 + mins
                        diff = (candidate_minutes - cur_minutes) % (24 * 60)

                        if 0 < diff < min_diff:
                            min_diff = diff
                            result = f"{hours:02d}:{mins:02d}"

        return result
