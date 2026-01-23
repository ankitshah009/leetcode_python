#956. Tallest Billboard
#Hard
#
#You are installing a billboard and want it supported by two steel supports, one
#on each side. Each support must be an equal height.
#
#You are given a collection of rods that can be welded together. Return the
#largest possible height of your billboard installation. If you cannot support
#the billboard, return 0.
#
#Example 1:
#Input: rods = [1,2,3,6]
#Output: 6
#Explanation: We have two disjoint subsets {1,2,3} and {6}, both sum to 6.
#
#Example 2:
#Input: rods = [1,2,3,4,5,6]
#Output: 10
#Explanation: We have two disjoint subsets {2,3,5} and {4,6}, both sum to 10.
#
#Example 3:
#Input: rods = [1,2]
#Output: 0
#
#Constraints:
#    1 <= rods.length <= 20
#    1 <= rods[i] <= 1000
#    sum(rods[i]) <= 5000

class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        """
        DP: dp[diff] = max height of shorter support when difference is diff.
        """
        # dp[diff] = max sum of shorter support
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()

            for diff, shorter in dp.items():
                taller = shorter + diff

                # Add rod to taller support
                new_diff = diff + rod
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), shorter)

                # Add rod to shorter support
                new_diff = abs(diff - rod)
                new_shorter = min(shorter + rod, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_shorter)

            dp = new_dp

        return dp[0]


class SolutionMemo:
    """Memoization approach"""

    def tallestBillboard(self, rods: list[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(idx: int, diff: int) -> int:
            """Return max height of shorter support."""
            if idx == len(rods):
                return 0 if diff == 0 else float('-inf')

            rod = rods[idx]

            # Don't use this rod
            skip = dp(idx + 1, diff)

            # Add to taller support (increase diff)
            add_taller = dp(idx + 1, diff + rod)

            # Add to shorter support (may change which is taller)
            add_shorter = dp(idx + 1, abs(diff - rod))
            if diff >= rod:
                add_shorter += rod
            else:
                add_shorter += diff

            return max(skip, add_taller, add_shorter)

        return dp(0, 0)


class SolutionMeetMiddle:
    """Meet in the middle for optimization"""

    def tallestBillboard(self, rods: list[int]) -> int:
        def get_states(rods):
            """Return dict: diff -> max shorter height"""
            states = {0: 0}

            for rod in rods:
                new_states = {}
                for diff, shorter in states.items():
                    taller = shorter + diff

                    # Don't use rod
                    key = diff
                    new_states[key] = max(new_states.get(key, 0), shorter)

                    # Add to taller
                    key = diff + rod
                    new_states[key] = max(new_states.get(key, 0), shorter)

                    # Add to shorter
                    key = abs(diff - rod)
                    new_shorter = min(shorter + rod, taller)
                    new_states[key] = max(new_states.get(key, 0), new_shorter)

                states = new_states

            return states

        n = len(rods)
        left = get_states(rods[:n // 2])
        right = get_states(rods[n // 2:])

        result = 0
        for diff, shorter in left.items():
            if diff in right:
                # Combine: left taller by diff, right shorter by same diff
                result = max(result, shorter + diff + right[diff])

        return result
