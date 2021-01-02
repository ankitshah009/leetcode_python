#754. Reach a Number
#Medium
#
#You are standing at position 0 on an infinite number line. There is a goal at position target.
#
#On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
#
#Return the minimum number of steps required to reach the destination.
#
#Example 1:
#
#Input: target = 3
#Output: 2
#Explanation:
#On the first move we step from 0 to 1.
#On the second step we step from 1 to 3.
#
#Example 2:
#
#Input: target = 2
#Output: 3
#Explanation:
#On the first move we step from 0 to 1.
#On the second move we step  from 1 to -1.
#On the third move we step from -1 to 2.
#
#Note:
#target will be a non-zero integer in the range [-10^9, 10^9].

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(math.ceil((math.sqrt(8 * target + 1) - 1) / 2)) # solve inequation: n * (n + 1) / 2 >= target
        d = n * (1 + n) // 2 - target
        if d % 2 == 0:
            # diff is even, always can flip a number from positive to negative
            return n
        else:
            # diff is odd, add more to make diff even, two condition:
            # 2: (1, -2, 3)
            # n = 2, 1 + 2 = 3, diff = 1, next n is 3, we can add 3 and flip one previous number, so only need extra 1 op
            # 5: (1, 2, 3, 4, -5)
            # n = 3, 1 + 2 + 3 = 6, diff = 1, add 4, 5, diff = 10, flip 5 to -5, done, two extra op
            return n + n % 2 + 1

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2
