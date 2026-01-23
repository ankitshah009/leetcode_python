#1815. Maximum Number of Groups Getting Fresh Donuts
#Hard
#
#There is a donuts shop that bakes donuts in batches of batchSize. They have a
#rule where they must serve all of the donuts of a batch before serving any
#donuts of the next batch. You are given an integer batchSize and an integer
#array groups, where groups[i] denotes that there is a group of groups[i]
#customers that will visit the shop. Each customer will get exactly one donut.
#
#When a group visits the shop, all customers of the group must be served before
#serving any of the following groups. A group will be happy if they all get
#fresh donuts. That is, the first customer of the group does not receive a
#donut that was left over from the previous group.
#
#You can freely rearrange the ordering of the groups. Return the maximum
#possible number of happy groups after rearranging the groups.
#
#Example 1:
#Input: batchSize = 3, groups = [1,2,3,4,5,6]
#Output: 4
#
#Example 2:
#Input: batchSize = 4, groups = [1,4,3,2]
#Output: 4
#
#Constraints:
#    1 <= batchSize <= 9
#    1 <= groups.length <= 30
#    1 <= groups[i] <= 10^9

from typing import List
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        """
        DP with memoization on remainder counts.
        """
        # Convert to remainders
        remainders = [g % batchSize for g in groups]

        # Count each remainder
        count = [0] * batchSize
        for r in remainders:
            count[r] += 1

        # Groups with remainder 0 are always happy
        happy = count[0]
        count[0] = 0

        # Pair complementary remainders
        for r in range(1, (batchSize + 1) // 2):
            comp = batchSize - r
            if r == comp:
                pairs = count[r] // 2
                happy += pairs
                count[r] -= pairs * 2
            else:
                pairs = min(count[r], count[comp])
                happy += pairs
                count[r] -= pairs
                count[comp] -= pairs

        # DP for remaining
        @lru_cache(maxsize=None)
        def dp(state: tuple, left_over: int) -> int:
            state = list(state)
            max_happy = 0

            for r in range(1, batchSize):
                if state[r] > 0:
                    state[r] -= 1
                    new_left = (left_over + r) % batchSize
                    extra = 1 if left_over == 0 else 0
                    max_happy = max(max_happy, extra + dp(tuple(state), new_left))
                    state[r] += 1

            return max_happy

        return happy + dp(tuple(count), 0)


class SolutionSimpler:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        """
        Simplified memoization approach.
        """
        from collections import Counter

        remainders = [g % batchSize for g in groups]
        count = Counter(remainders)

        # Handle remainder 0
        result = count[0]
        del count[0]

        @lru_cache(maxsize=None)
        def dp(counts: tuple, leftover: int) -> int:
            counts = list(counts)
            best = 0

            for r in range(1, batchSize):
                if counts[r-1] > 0:
                    counts[r-1] -= 1
                    happy = 1 if leftover == 0 else 0
                    new_left = (leftover + r) % batchSize
                    best = max(best, happy + dp(tuple(counts), new_left))
                    counts[r-1] += 1

            return best

        initial = tuple(count.get(r, 0) for r in range(1, batchSize))
        return result + dp(initial, 0)
