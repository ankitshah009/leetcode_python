#330. Patching Array
#Hard
#
#Given a sorted integer array nums and an integer n, add/patch elements to the
#array such that any number in the range [1, n] inclusive can be formed by the
#sum of some elements in the array.
#
#Return the minimum number of patches required.
#
#Example 1:
#Input: nums = [1,3], n = 6
#Output: 1
#Explanation: Combinations of nums are [1], [3], [1,3], which form possible
#sums of: 1, 3, 4. Now if we add/patch 2 to nums, the combinations are:
#[1], [2], [3], [1,3], [2,3], [1,2,3]. Possible sums are 1, 2, 3, 4, 5, 6,
#which now covers the range [1, 6]. So we only need 1 patch.
#
#Example 2:
#Input: nums = [1,5,10], n = 20
#Output: 2
#Explanation: The two patches can be [2, 4].
#
#Example 3:
#Input: nums = [1,2,2], n = 5
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 10^4
#    nums is sorted in ascending order.
#    1 <= n <= 2^31 - 1

from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        Greedy approach.
        Key insight: If we can form all numbers in [1, miss-1], and we have
        a number x <= miss, then we can form all numbers in [1, miss + x - 1].

        If x > miss, we need to add miss to extend our range.
        """
        patches = 0
        i = 0
        miss = 1  # Smallest number we can't form yet

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # Use nums[i] to extend our range
                miss += nums[i]
                i += 1
            else:
                # Need to add miss as a patch
                miss += miss  # Now we can form [1, 2*miss - 1]
                patches += 1

        return patches


class SolutionDetailed:
    """More detailed explanation"""

    def minPatches(self, nums: List[int], n: int) -> int:
        # 'reach' represents the maximum sum we can form with current numbers
        # Initially, we can form sums in range [0, 0] (just 0, nothing selected)
        reach = 0
        patches = 0
        i = 0

        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                # We can use nums[i] to extend our reach
                # With nums[i], we can form sums in [0, reach + nums[i]]
                reach += nums[i]
                i += 1
            else:
                # We need to patch with (reach + 1)
                # This extends our reach to [0, 2 * reach + 1]
                patches += 1
                reach = 2 * reach + 1

        return patches
