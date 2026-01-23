#1742. Maximum Number of Balls in a Box
#Easy
#
#You are working in a ball factory where you have n balls numbered from
#lowLimit to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and
#an infinite number of boxes numbered from 1 to infinity.
#
#Your job is to put each ball in the box with a number equal to the sum of
#digits of the ball's number. For example, ball 321 will be put in box 6 because
#3 + 2 + 1 = 6.
#
#Given two integers lowLimit and highLimit, return the number of balls in the
#box with the most balls.
#
#Example 1:
#Input: lowLimit = 1, highLimit = 10
#Output: 2
#
#Example 2:
#Input: lowLimit = 5, highLimit = 15
#Output: 2
#
#Example 3:
#Input: lowLimit = 19, highLimit = 28
#Output: 2
#
#Constraints:
#    1 <= lowLimit <= highLimit <= 10^5

from collections import Counter

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        Count digit sums for each number.
        """
        def digit_sum(n: int) -> int:
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        box_count = Counter(digit_sum(i) for i in range(lowLimit, highLimit + 1))
        return max(box_count.values())


class SolutionArray:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        Using array instead of Counter (max digit sum for 10^5 is 45).
        """
        boxes = [0] * 46

        for ball in range(lowLimit, highLimit + 1):
            digit_sum = sum(int(d) for d in str(ball))
            boxes[digit_sum] += 1

        return max(boxes)


class SolutionOptimized:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        Optimized digit sum calculation - increment instead of recalculating.
        """
        boxes = [0] * 46

        # Calculate initial digit sum
        current_sum = sum(int(d) for d in str(lowLimit))
        boxes[current_sum] += 1

        # Increment through range
        for ball in range(lowLimit + 1, highLimit + 1):
            # Adjust digit sum based on change from previous number
            temp = ball
            add = 1
            while temp % 10 == 0:
                add -= 9  # Went from 9 to 0
                temp //= 10

            current_sum += add
            boxes[current_sum] += 1

        return max(boxes)
