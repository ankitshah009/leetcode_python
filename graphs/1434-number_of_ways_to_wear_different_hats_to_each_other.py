#1434. Number of Ways to Wear Different Hats to Each Other
#Hard
#
#There are n people and 40 types of hats labeled from 1 to 40.
#
#Given a 2D integer array hats, where hats[i] is a list of all hats preferred
#by the i-th person.
#
#Return the number of ways that the n people wear different hats to each other.
#
#Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: hats = [[3,4],[4,5],[5]]
#Output: 1
#Explanation: There is only one way to choose hats given the conditions.
#First person choose hat 3, Second person choose hat 4 and last one hat 5.
#
#Example 2:
#Input: hats = [[3,5,1],[3,5]]
#Output: 4
#Explanation: There are 4 ways to choose hats:
#(3,5), (5,3), (1,3) and (1,5)
#
#Example 3:
#Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#Output: 24
#Explanation: Each person can choose hats labeled from 1 to 4.
#Number of Permutations of (1,2,3,4) = 24.
#
#Constraints:
#    n == hats.length
#    1 <= n <= 10
#    1 <= hats[i].length <= 40
#    1 <= hats[i][j] <= 40
#    hats[i] contains a list of unique integers.

from typing import List
from functools import lru_cache

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        """
        Bitmask DP where mask represents which people have hats.
        Iterate over hats (1-40), for each hat, assign to eligible people.
        O(40 * 2^n * n) time.
        """
        MOD = 10**9 + 7
        n = len(hats)

        # hat_to_people: which people can wear each hat
        hat_to_people = [[] for _ in range(41)]
        for person in range(n):
            for hat in hats[person]:
                hat_to_people[hat].append(person)

        # dp[mask] = number of ways to achieve this mask of people with hats
        target_mask = (1 << n) - 1

        @lru_cache(maxsize=None)
        def dp(hat: int, mask: int) -> int:
            # All people have hats
            if mask == target_mask:
                return 1

            # No more hats to try
            if hat > 40:
                return 0

            # Option 1: Don't use this hat
            ways = dp(hat + 1, mask)

            # Option 2: Give this hat to an eligible person who doesn't have a hat
            for person in hat_to_people[hat]:
                if not (mask & (1 << person)):
                    ways = (ways + dp(hat + 1, mask | (1 << person))) % MOD

            return ways

        return dp(1, 0)


class SolutionIterative:
    def numberWays(self, hats: List[List[int]]) -> int:
        """Iterative DP"""
        MOD = 10**9 + 7
        n = len(hats)
        target = (1 << n) - 1

        # hat_to_people
        hat_to_people = [[] for _ in range(41)]
        for person in range(n):
            for hat in hats[person]:
                hat_to_people[hat].append(person)

        # dp[mask] = ways to achieve mask
        dp = [0] * (1 << n)
        dp[0] = 1

        for hat in range(1, 41):
            # Process in reverse to avoid using same hat twice
            for mask in range(target, -1, -1):
                if dp[mask] == 0:
                    continue

                for person in hat_to_people[hat]:
                    if not (mask & (1 << person)):
                        new_mask = mask | (1 << person)
                        dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

        return dp[target]


class SolutionAlt:
    def numberWays(self, hats: List[List[int]]) -> int:
        """Alternative formulation"""
        MOD = 10**9 + 7
        n = len(hats)

        # Convert to hat -> set of people
        hat_people = [set() for _ in range(41)]
        for i, h_list in enumerate(hats):
            for h in h_list:
                hat_people[h].add(i)

        # DP
        all_people = (1 << n) - 1
        dp = {0: 1}

        for hat in range(1, 41):
            if not hat_people[hat]:
                continue

            new_dp = dict(dp)  # Copy current state

            for mask, ways in dp.items():
                for person in hat_people[hat]:
                    if not (mask & (1 << person)):
                        new_mask = mask | (1 << person)
                        new_dp[new_mask] = (new_dp.get(new_mask, 0) + ways) % MOD

            dp = new_dp

        return dp.get(all_people, 0)
