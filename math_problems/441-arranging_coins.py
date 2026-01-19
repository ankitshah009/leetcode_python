#441. Arranging Coins
#Easy
#
#You have n coins and you want to build a staircase with these coins. The staircase consists
#of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#
#Given the integer n, return the number of complete rows of the staircase you will build.
#
#Example 1:
#Input: n = 5
#Output: 2
#Explanation: Because the 3rd row is incomplete, we return 2.
#
#Example 2:
#Input: n = 8
#Output: 3
#Explanation: Because the 4th row is incomplete, we return 3.
#
#Constraints:
#    1 <= n <= 2^31 - 1

import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Using quadratic formula: k*(k+1)/2 <= n
        # k^2 + k - 2n <= 0
        # k = (-1 + sqrt(1 + 8n)) / 2
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)

    def arrangeCoins_binary_search(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            coins_needed = mid * (mid + 1) // 2

            if coins_needed == n:
                return mid
            elif coins_needed < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
