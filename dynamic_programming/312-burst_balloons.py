#312. Burst Balloons
#Hard
#
#You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it
#represented by an array nums. You are asked to burst all the balloons.
#
#If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
#If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon
#with a 1 painted on it.
#
#Return the maximum coins you can collect by bursting the balloons wisely.
#
#Example 1:
#Input: nums = [3,1,5,8]
#Output: 167
#Explanation:
#nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
#coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
#Example 2:
#Input: nums = [1,5]
#Output: 10
#
#Constraints:
#    n == nums.length
#    1 <= n <= 300
#    0 <= nums[i] <= 100

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1s at boundaries
        nums = [1] + nums + [1]
        n = len(nums)

        # dp[i][j] = max coins from bursting all balloons between i and j (exclusive)
        dp = [[0] * n for _ in range(n)]

        # Iterate over all possible lengths
        for length in range(2, n):  # length is the gap between i and j
            for i in range(n - length):
                j = i + length
                # Try bursting each balloon k last in the range (i, j)
                for k in range(i + 1, j):
                    coins = nums[i] * nums[k] * nums[j]
                    coins += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)

        return dp[0][n - 1]
