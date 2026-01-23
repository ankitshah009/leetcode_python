#1014. Best Sightseeing Pair
#Medium
#
#You are given an integer array values where values[i] represents the value of
#the i-th sightseeing spot. Two sightseeing spots i and j have a distance j - i
#between them.
#
#The score of a pair (i < j) of sightseeing spots is values[i] + values[j] +
#i - j, which is (values[i] + i) + (values[j] - j).
#
#Return the maximum score of a pair of sightseeing spots.
#
#Example 1:
#Input: values = [8,1,5,2,6]
#Output: 11
#Explanation: i = 0, j = 2, values[0] + values[2] + 0 - 2 = 8 + 5 - 2 = 11
#
#Example 2:
#Input: values = [1,2]
#Output: 2
#
#Constraints:
#    2 <= values.length <= 5 * 10^4
#    1 <= values[i] <= 1000

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        Track max(values[i] + i) for left part.
        """
        max_left = values[0]  # values[i] + i
        max_score = 0

        for j in range(1, len(values)):
            # Score for pair ending at j
            max_score = max(max_score, max_left + values[j] - j)
            # Update max_left
            max_left = max(max_left, values[j] + j)

        return max_score


class SolutionExplicit:
    """More explicit formulation"""

    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)

        # Precompute values[i] + i
        left_scores = [values[i] + i for i in range(n)]

        max_left = left_scores[0]
        result = 0

        for j in range(1, n):
            right_score = values[j] - j
            result = max(result, max_left + right_score)
            max_left = max(max_left, left_scores[j])

        return result


class SolutionDP:
    """DP approach"""

    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)

        # dp[j] = max score ending at j
        # Need max(values[i] + i) for i < j

        max_prefix = [0] * n
        max_prefix[0] = values[0]

        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i - 1], values[i] + i)

        result = 0
        for j in range(1, n):
            result = max(result, max_prefix[j - 1] + values[j] - j)

        return result
