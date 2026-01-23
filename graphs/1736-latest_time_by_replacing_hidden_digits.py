#1736. Latest Time by Replacing Hidden Digits
#Easy
#
#You are given a string time in the form of hh:mm, where some of the digits in
#the string are hidden (represented by ?).
#
#The valid times are those inclusively between 00:00 and 23:59.
#
#Return the latest valid time you can get from time by replacing the hidden
#digits.
#
#Example 1:
#Input: time = "2?:?0"
#Output: "23:50"
#
#Example 2:
#Input: time = "0?:3?"
#Output: "09:39"
#
#Example 3:
#Input: time = "1?:22"
#Output: "19:22"
#
#Constraints:
#    time is in the format hh:mm.
#    It is guaranteed that you can produce a valid time from the given string.

class Solution:
    def maximumTime(self, time: str) -> str:
        """
        Replace each ? with maximum valid digit.
        """
        time = list(time)

        # First digit of hour
        if time[0] == '?':
            # If second digit is 0-3 or ?, first can be 2
            # Otherwise first must be 1
            time[0] = '2' if time[1] in '?0123' else '1'

        # Second digit of hour
        if time[1] == '?':
            # If first digit is 2, second can be at most 3
            # Otherwise second can be 9
            time[1] = '3' if time[0] == '2' else '9'

        # First digit of minute
        if time[3] == '?':
            time[3] = '5'

        # Second digit of minute
        if time[4] == '?':
            time[4] = '9'

        return ''.join(time)


class SolutionBruteForce:
    def maximumTime(self, time: str) -> str:
        """
        Try all valid times from latest to earliest.
        """
        def matches(t: str, pattern: str) -> bool:
            for tc, pc in zip(t, pattern):
                if pc != '?' and tc != pc:
                    return False
            return True

        # Try from 23:59 down to 00:00
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                if matches(t, time):
                    return t

        return ""


class SolutionRegex:
    def maximumTime(self, time: str) -> str:
        """
        Using regex pattern matching.
        """
        import re

        pattern = time.replace('?', '.')

        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                if re.fullmatch(pattern, t):
                    return t

        return ""
