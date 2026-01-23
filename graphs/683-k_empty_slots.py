#683. K Empty Slots
#Hard
#
#You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are
#turned off. We turn on exactly one bulb every day until all bulbs are on after
#n days.
#
#You are given an array bulbs of length n where bulbs[i] = x means that on the
#(i+1)th day, we will turn on the bulb at position x where i is 0-indexed and
#x is 1-indexed.
#
#Given an integer k, return the minimum day number such that there exists two
#turned on bulbs that have exactly k bulbs between them that are all turned off.
#If there isn't such day, return -1.
#
#Example 1:
#Input: bulbs = [1,3,2], k = 1
#Output: 2
#Explanation: On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
#On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
#On the second day, there are two on bulbs with one off bulb between them.
#
#Example 2:
#Input: bulbs = [1,2,3], k = 1
#Output: -1
#
#Constraints:
#    n == bulbs.length
#    1 <= n <= 2 * 10^4
#    1 <= bulbs[i] <= n
#    bulbs is a permutation of numbers from 1 to n
#    0 <= k <= 2 * 10^4

from sortedcontainers import SortedList

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        """
        Use sorted set to track turned on positions.
        For each new bulb, check neighbors.
        """
        on = SortedList()

        for day, pos in enumerate(bulbs, 1):
            idx = on.bisect_left(pos)

            # Check right neighbor
            if idx < len(on) and on[idx] - pos == k + 1:
                return day

            # Check left neighbor
            if idx > 0 and pos - on[idx - 1] == k + 1:
                return day

            on.add(pos)

        return -1


class SolutionSlidingWindow:
    """
    Sliding window approach using days array.
    For window [left, right] with size k+2, check if all middle elements
    have days greater than both endpoints.
    """

    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        n = len(bulbs)
        # days[i] = day when position i+1 is turned on
        days = [0] * n
        for day, pos in enumerate(bulbs):
            days[pos - 1] = day

        result = float('inf')
        left, right = 0, k + 1

        while right < n:
            valid = True
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    valid = False
                    left = i
                    right = i + k + 1
                    break

            if valid:
                result = min(result, max(days[left], days[right]) + 1)
                left = right
                right = left + k + 1

        return result if result != float('inf') else -1
