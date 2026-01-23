#1010. Pairs of Songs With Total Durations Divisible by 60
#Medium
#
#You are given a list of songs where the i-th song has a duration of time[i]
#seconds.
#
#Return the number of pairs of songs for which their total duration in seconds
#is divisible by 60. Formally, we want the number of indices i, j such that
#i < j with (time[i] + time[j]) % 60 == 0.
#
#Example 1:
#Input: time = [30,20,150,100,40]
#Output: 3
#Explanation: Pairs (0,2), (1,3), (1,4) have totals 180, 120, 60.
#
#Example 2:
#Input: time = [60,60,60]
#Output: 3
#
#Constraints:
#    1 <= time.length <= 6 * 10^4
#    1 <= time[i] <= 500

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        """
        Count remainders, pair complementary remainders.
        """
        remainder_count = [0] * 60
        count = 0

        for t in time:
            r = t % 60
            complement = (60 - r) % 60  # Handle r=0 case
            count += remainder_count[complement]
            remainder_count[r] += 1

        return count


class SolutionTwoSum:
    """Two-sum style"""

    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        count = [0] * 60
        result = 0

        for t in time:
            r = t % 60
            # Find complement
            if r == 0:
                result += count[0]
            else:
                result += count[60 - r]
            count[r] += 1

        return result


class SolutionCounting:
    """Count then combine"""

    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        count = [0] * 60

        for t in time:
            count[t % 60] += 1

        result = 0

        # Pairs with remainder 0: C(n,2)
        result += count[0] * (count[0] - 1) // 2

        # Pairs with remainder 30: C(n,2)
        result += count[30] * (count[30] - 1) // 2

        # Complementary pairs (1+59, 2+58, ..., 29+31)
        for i in range(1, 30):
            result += count[i] * count[60 - i]

        return result
