#1775. Equal Sum Arrays With Minimum Number of Operations
#Medium
#
#You are given two arrays of integers nums1 and nums2, possibly of different
#lengths. The values in the arrays are between 1 and 6, inclusive.
#
#In one operation, you can change any integer's value in any of the arrays to
#any value between 1 and 6, inclusive.
#
#Return the minimum number of operations required to make the sum of values in
#nums1 equal to the sum of values in nums2. Return -1 if it is not possible to
#make the sum of the two arrays equal.
#
#Example 1:
#Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
#Output: 3
#
#Example 2:
#Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
#Output: -1
#
#Example 3:
#Input: nums1 = [6,6], nums2 = [1]
#Output: 3
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 10^5
#    1 <= nums1[i], nums2[i] <= 6

from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Greedy: use operations with maximum gain first.
        """
        sum1, sum2 = sum(nums1), sum(nums2)

        # Make sum1 the larger one
        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        diff = sum1 - sum2

        if diff == 0:
            return 0

        # Check if possible
        # Max we can reduce: nums1 all to 1, nums2 all to 6
        max_reduce = sum1 - len(nums1) + len(nums2) * 6 - sum2
        if max_reduce < diff:
            return -1

        # Count potential gains
        # From nums1: reduce x to 1 -> gain = x - 1
        # From nums2: increase x to 6 -> gain = 6 - x
        gains = []
        for x in nums1:
            gains.append(x - 1)
        for x in nums2:
            gains.append(6 - x)

        # Sort gains descending, greedily pick until diff covered
        gains.sort(reverse=True)

        ops = 0
        for gain in gains:
            if diff <= 0:
                break
            diff -= gain
            ops += 1

        return ops


class SolutionCounting:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Counting sort for gains.
        """
        sum1, sum2 = sum(nums1), sum(nums2)

        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        diff = sum1 - sum2
        if diff == 0:
            return 0

        # Count frequencies
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        # Count gains by amount (1 to 5)
        gain_count = [0] * 6
        for val, count in cnt1.items():
            gain_count[val - 1] += count  # Reduce val to 1
        for val, count in cnt2.items():
            gain_count[6 - val] += count  # Increase val to 6

        ops = 0
        for gain in range(5, 0, -1):
            if diff <= 0:
                break
            # Use as many of this gain as needed
            use = min(gain_count[gain], (diff + gain - 1) // gain)
            ops += use
            diff -= use * gain

        return ops if diff <= 0 else -1
