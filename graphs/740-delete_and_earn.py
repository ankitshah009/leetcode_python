#740. Delete and Earn
#Medium
#
#You are given an integer array nums. You want to maximize the number of points
#you get by performing the following operation any number of times:
#
#Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
#delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
#
#Return the maximum number of points you can earn by applying the above operation
#some number of times.
#
#Example 1:
#Input: nums = [3,4,2]
#Output: 6
#Explanation: You can perform the following operations:
#- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
#- Delete 2 to earn 2 points. nums = [].
#You earn a total of 6 points.
#
#Example 2:
#Input: nums = [2,2,3,3,3,4]
#Output: 9
#Explanation: You can perform the following operations:
#- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
#- Delete a 3 to earn 3 points. nums = [3].
#- Delete a 3 to earn 3 points. nums = [].
#You earn a total of 9 points.
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    1 <= nums[i] <= 10^4

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Transform to house robber problem: can't take adjacent values.
        """
        count = Counter(nums)
        max_num = max(nums)

        # points[i] = total points from taking all instances of i
        points = [0] * (max_num + 1)
        for num, cnt in count.items():
            points[num] = num * cnt

        # House robber DP
        prev, curr = 0, 0

        for i in range(max_num + 1):
            prev, curr = curr, max(curr, prev + points[i])

        return curr


class SolutionSorted:
    """Handle sparse arrays by sorting unique values"""

    def deleteAndEarn(self, nums: list[int]) -> int:
        count = Counter(nums)
        sorted_nums = sorted(count.keys())

        prev, curr = 0, 0

        for i, num in enumerate(sorted_nums):
            points = num * count[num]

            if i > 0 and sorted_nums[i - 1] == num - 1:
                # Adjacent, can't take both
                prev, curr = curr, max(curr, prev + points)
            else:
                # Not adjacent, can take this for free
                prev, curr = curr, curr + points

        return curr


class SolutionDP:
    """Explicit DP array"""

    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0

        count = Counter(nums)
        max_num = max(nums)

        # dp[i] = max points considering values up to i
        dp = [0] * (max_num + 2)

        for i in range(1, max_num + 1):
            points = i * count.get(i, 0)
            dp[i] = max(dp[i - 1], dp[i - 2] + points)

        return dp[max_num]
