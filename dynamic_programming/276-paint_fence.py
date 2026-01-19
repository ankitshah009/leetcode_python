#276. Paint Fence
#Medium
#
#You are painting a fence of n posts with k different colors. You must paint the
#posts such that no more than two adjacent fence posts have the same color.
#
#Given the two integers n and k, return the number of ways you can paint the fence.
#
#Example 1:
#Input: n = 3, k = 2
#Output: 6
#Explanation: All the possibilities are:
#Post 1  Post 2  Post 3
#  1       1       2
#  1       2       1
#  1       2       2
#  2       1       1
#  2       1       2
#  2       2       1
#
#Example 2:
#Input: n = 1, k = 1
#Output: 1
#
#Example 3:
#Input: n = 7, k = 2
#Output: 42
#
#Constraints:
#    1 <= n <= 50
#    1 <= k <= 10^5
#    The testcases are generated such that the answer is in the range [0, 2^31 - 1]

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        # same[i] = ways to paint i posts where last 2 posts are same color
        # diff[i] = ways to paint i posts where last 2 posts are different colors

        # For post i:
        # same[i] = diff[i-1] (can only have same if previous two were different)
        # diff[i] = (same[i-1] + diff[i-1]) * (k-1) (can use any other color)

        same = k  # For 2 posts: k ways to have same color
        diff = k * (k - 1)  # For 2 posts: k * (k-1) ways to have different colors

        for i in range(3, n + 1):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff

        return same + diff

    # Alternative: single variable approach
    def numWaysSimplified(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k

        # total[i] = same[i] + diff[i]
        # total[i] = diff[i-1] + (total[i-1]) * (k-1)
        # total[i] = total[i-1] * (k-1) + total[i-2] * (k-1)
        # total[i] = (k-1) * (total[i-1] + total[i-2])

        prev2, prev1 = k, k * k

        for i in range(3, n + 1):
            curr = (k - 1) * (prev1 + prev2)
            prev2, prev1 = prev1, curr

        return prev1
