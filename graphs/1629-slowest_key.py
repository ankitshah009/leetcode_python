#1629. Slowest Key
#Easy
#
#A newly designed keypad was tested, where a tester pressed a sequence of n keys,
#one at a time.
#
#You are given a string keysPressed of length n, where keysPressed[i] was the
#ith key pressed in the testing sequence, and a sorted list releaseTimes, where
#releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed.
#The 0th key was pressed at the time 0, and every subsequent key was pressed at
#the exact time the previous key was released.
#
#The tester wants to know the key of the keypress that had the longest duration.
#The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and
#the 0th keypress had a duration of releaseTimes[0].
#
#Note that the same key could have been pressed multiple times during the test,
#and these multiple presses of the same key may not have had the same duration.
#
#Return the key of the keypress that had the longest duration. If there are
#multiple such keypresses, return the lexicographically largest key of the
#keypresses.
#
#Example 1:
#Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
#Output: "c"
#Explanation: The keypresses were as follows:
#Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
#Keypress for 'b' had a duration of 29 - 9 = 20.
#Keypress for 'c' had a duration of 49 - 29 = 20.
#Keypress for 'd' had a duration of 50 - 49 = 1.
#The longest is 'b' and the second 'c' with duration 20.
#'c' is lexicographically larger than 'b', so the answer is 'c'.
#
#Example 2:
#Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
#Output: "a"
#Explanation: All keys have the same duration of about 12.
#'a' is lexicographically largest.
#
#Constraints:
#    releaseTimes.length == n
#    keysPressed.length == n
#    2 <= n <= 1000
#    1 <= releaseTimes[i] <= 10^9
#    releaseTimes[i] < releaseTimes[i+1]
#    keysPressed contains only lowercase English letters.

from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Calculate duration for each keypress, track max duration and key.
        """
        n = len(releaseTimes)

        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]

        for i in range(1, n):
            duration = releaseTimes[i] - releaseTimes[i - 1]

            if duration > max_duration or (duration == max_duration and keysPressed[i] > slowest_key):
                max_duration = duration
                slowest_key = keysPressed[i]

        return slowest_key


class SolutionTuple:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Using tuple comparison for cleaner code.
        """
        n = len(releaseTimes)
        durations = [releaseTimes[0]] + [
            releaseTimes[i] - releaseTimes[i - 1]
            for i in range(1, n)
        ]

        # Find max by (duration, key)
        best = max(zip(durations, keysPressed))
        return best[1]


class SolutionZip:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Using zip and max with key function.
        """
        prev = 0
        result = ('', 0)  # (key, duration)

        for time, key in zip(releaseTimes, keysPressed):
            duration = time - prev
            prev = time

            if (duration, key) > (result[1], result[0]):
                result = (key, duration)

        return result[0]


class SolutionOneLiner:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Compact one-liner solution.
        """
        return max(
            zip(keysPressed, [releaseTimes[0]] + [
                releaseTimes[i] - releaseTimes[i-1]
                for i in range(1, len(releaseTimes))
            ]),
            key=lambda x: (x[1], x[0])
        )[0]
