#837. New 21 Game
#Medium
#
#Alice plays the following game, loosely based on the card game "21".
#
#Alice starts with 0 points and draws numbers while she has less than k points.
#During each draw, she gains an integer number of points randomly from the range
#[1, maxPts], where maxPts is an integer. Each draw is independent and the
#outcomes have equal probabilities.
#
#Alice stops drawing numbers when she gets k or more points.
#
#Return the probability that Alice has n or fewer points.
#
#Example 1:
#Input: n = 10, k = 1, maxPts = 10
#Output: 1.00000
#Explanation: Alice gets a single card, then stops.
#
#Example 2:
#Input: n = 6, k = 1, maxPts = 10
#Output: 0.60000
#
#Example 3:
#Input: n = 21, k = 17, maxPts = 10
#Output: 0.73278
#
#Constraints:
#    0 <= k <= n <= 10^4
#    1 <= maxPts <= 10^4

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        DP with sliding window.
        dp[i] = probability of reaching exactly i points.
        dp[i] = (dp[i-1] + dp[i-2] + ... + dp[i-maxPts]) / maxPts
        for i in [k, k+maxPts-1], can only reach from points < k.
        """
        if k == 0 or n >= k + maxPts:
            return 1.0

        # dp[i] = probability of reaching i points before stopping
        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window_sum = 1.0  # Sum of dp[i-maxPts:i]
        prob = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            else:
                prob += dp[i]

            if i >= maxPts:
                window_sum -= dp[i - maxPts]

        return prob


class SolutionReverse:
    """Compute from end"""

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        # dp[i] = probability of having <= n points when starting at i
        dp = [0.0] * (k + maxPts)

        # Base cases: points in [k, n] have probability 1
        for i in range(k, min(n + 1, k + maxPts)):
            dp[i] = 1.0

        # Window sum for sliding window
        window_sum = sum(dp[k:k + maxPts])

        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts
            # Update window
            window_sum += dp[i]
            window_sum -= dp[i + maxPts]

        return dp[0]
