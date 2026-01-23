#611. Valid Triangle Number
#Medium
#
#Given an integer array nums, return the number of triplets chosen from the array
#that can make triangles if we take them as side lengths of a triangle.
#
#Example 1:
#Input: nums = [2,2,3,4]
#Output: 3
#Explanation: Valid combinations are:
#2,3,4 (using the first 2)
#2,3,4 (using the second 2)
#2,2,3
#
#Example 2:
#Input: nums = [4,2,3,4]
#Output: 4
#
#Constraints:
#    1 <= nums.length <= 1000
#    0 <= nums[i] <= 1000

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Sort and use two pointers.
        For valid triangle: a + b > c (where a <= b <= c)
        Fix c, use two pointers for a and b.
        """
        nums.sort()
        count = 0
        n = len(nums)

        for k in range(n - 1, 1, -1):
            c = nums[k]
            i, j = 0, k - 1

            while i < j:
                if nums[i] + nums[j] > c:
                    # All pairs (i, i+1, ..., j-1) with j work
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count


class SolutionBinarySearch:
    """Binary search approach"""

    def triangleNumber(self, nums: List[int]) -> int:
        import bisect

        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            if nums[i] == 0:
                continue
            for j in range(i + 1, n - 1):
                # Find largest k where nums[k] < nums[i] + nums[j]
                target = nums[i] + nums[j]
                k = bisect.bisect_left(nums, target, j + 1, n)
                count += k - j - 1

        return count


class SolutionBruteForce:
    """O(n^3) brute force"""

    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
                    else:
                        break  # Since sorted, no more valid k

        return count
