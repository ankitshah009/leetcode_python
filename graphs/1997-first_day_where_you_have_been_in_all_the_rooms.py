#1997. First Day Where You Have Been in All the Rooms
#Medium
#
#There are n rooms you need to visit, labeled from 0 to n - 1. Each day is
#labeled, starting from 0. You will go in and visit one room a day.
#
#Initially on day 0, you visit room 0. The order you visit the rooms for the
#coming days is determined by the following rules and a given 0-indexed array
#nextVisit of length n:
#
#- Assuming that on a day, you visit room i,
#- if you have been in room i an odd number of times (including the current
#  visit), on the next day you will visit room nextVisit[i] where
#  0 <= nextVisit[i] <= i;
#- if you have been in room i an even number of times (including the current
#  visit), on the next day you will visit room (i + 1) mod n.
#
#Return the label of the first day where you have been in all the rooms. It can
#be shown that such a day exists. Since the answer may be very large, return it
#modulo 10^9 + 7.
#
#Example 1:
#Input: nextVisit = [0,0]
#Output: 2
#Explanation: Day 0: visit room 0. Visited rooms = {0}
#Day 1: visit room 0 (odd visits -> nextVisit[0] = 0). Visited rooms = {0}
#Day 2: visit room 1 (even visits -> next room). Visited rooms = {0,1}
#
#Example 2:
#Input: nextVisit = [0,0,2]
#Output: 6
#
#Example 3:
#Input: nextVisit = [0,1,2,0]
#Output: 6
#
#Constraints:
#    n == nextVisit.length
#    2 <= n <= 10^5
#    0 <= nextVisit[i] <= i

from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        """
        DP where dp[i] = first day we visit room i with even visits to i-1.

        Key insight: We visit room i for the first time only when we've
        visited room i-1 an even number of times.

        dp[i] = dp[i-1] + 1 + (dp[i-1] - dp[nextVisit[i-1]]) + 1

        Where:
        - dp[i-1]: days to first reach room i-1
        - +1: day to go from i-1 to nextVisit[i-1] (odd visit)
        - (dp[i-1] - dp[nextVisit[i-1]]): days to go from nextVisit[i-1] back to i-1
        - +1: day to go from i-1 to i (even visit)
        """
        MOD = 10**9 + 7
        n = len(nextVisit)

        # dp[i] = day when room i is first visited
        dp = [0] * n

        for i in range(1, n):
            # From room i-1, we need:
            # 1. One day to go to nextVisit[i-1] (odd visit count)
            # 2. Days to get back from nextVisit[i-1] to room i-1
            # 3. One day to move to room i (even visit count)
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD

        return dp[n - 1]


class SolutionExplained:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        """
        Detailed explanation:

        Let dp[i] = first day to reach room i.

        When we first reach room i-1:
        - We've visited it odd times (1), so we go to nextVisit[i-1]
        - To reach room i, we need to visit room i-1 even times

        Time to get back to room i-1 after going to nextVisit[i-1]:
        - Same as time to go from nextVisit[i-1] to room i-1 originally
        - That's dp[i-1] - dp[nextVisit[i-1]]

        So: dp[i] = dp[i-1] + 1 (go to nextVisit[i-1])
                  + (dp[i-1] - dp[nextVisit[i-1]]) (back to i-1)
                  + 1 (go to i)
                = 2*dp[i-1] - dp[nextVisit[i-1]] + 2
        """
        MOD = 10**9 + 7
        n = len(nextVisit)

        dp = [0] * n

        for i in range(1, n):
            # Days to first reach room i-1
            prev = dp[i - 1]
            # Days to first reach nextVisit[i-1]
            back = dp[nextVisit[i - 1]]

            # Total = prev + 1 + (prev - back) + 1
            dp[i] = (2 * prev - back + 2 + MOD) % MOD

        return dp[n - 1]
