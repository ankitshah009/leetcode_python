#1423. Maximum Points You Can Obtain from Cards
#Medium
#
#There are several cards arranged in a row, and each card has an associated
#number of points. The points are given in the integer array cardPoints.
#
#In one step, you can take one card from the beginning or from the end of the
#row. You have to take exactly k cards.
#
#Your score is the sum of the points of the cards you have taken.
#
#Given the integer array cardPoints and the integer k, return the maximum score
#you can obtain.
#
#Example 1:
#Input: cardPoints = [1,2,3,4,5,6,1], k = 3
#Output: 12
#Explanation: After the first step, your score will always be 1. However,
#choosing the rightmost card first will maximize your total score. The optimal
#strategy is to take the three cards on the right, giving a final score of
#1 + 6 + 5 = 12.
#
#Example 2:
#Input: cardPoints = [2,2,2], k = 2
#Output: 4
#Explanation: Regardless of which two cards you take, your score will always be 4.
#
#Example 3:
#Input: cardPoints = [9,7,7,9,7,7,9], k = 7
#Output: 55
#Explanation: You have to take all the cards. Your score is the sum of points of
#all cards.
#
#Constraints:
#    1 <= cardPoints.length <= 10^5
#    1 <= cardPoints[i] <= 10^4
#    1 <= k <= cardPoints.length

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Taking k cards from ends = leaving (n-k) cards in middle.
        Minimize sum of middle window to maximize sum of taken cards.
        """
        n = len(cardPoints)
        window_size = n - k

        if window_size == 0:
            return sum(cardPoints)

        total = sum(cardPoints)

        # Find minimum sum window of size (n-k)
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum

        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, window_sum)

        return total - min_window


class SolutionPrefixSum:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Take i cards from left and (k-i) from right, for i in [0, k].
        Use prefix and suffix sums.
        """
        n = len(cardPoints)

        # Prefix sum from left
        left_sum = [0] * (k + 1)
        for i in range(k):
            left_sum[i + 1] = left_sum[i] + cardPoints[i]

        # Suffix sum from right
        right_sum = [0] * (k + 1)
        for i in range(k):
            right_sum[i + 1] = right_sum[i] + cardPoints[n - 1 - i]

        # Maximum of taking i from left and (k-i) from right
        max_score = 0
        for i in range(k + 1):
            score = left_sum[i] + right_sum[k - i]
            max_score = max(max_score, score)

        return max_score


class SolutionSlidingWindow:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Sliding window over the k cards at ends.
        Start with k cards from left, then slide to right.
        """
        n = len(cardPoints)

        # Start with all k cards from left
        current_sum = sum(cardPoints[:k])
        max_sum = current_sum

        # Slide: remove one from left end of window, add one from right end
        for i in range(1, k + 1):
            # Remove cardPoints[k-i], add cardPoints[n-i]
            current_sum = current_sum - cardPoints[k - i] + cardPoints[n - i]
            max_sum = max(max_sum, current_sum)

        return max_sum
