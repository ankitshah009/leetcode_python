#697. Degree of an Array
#Easy
#
#Given a non-empty array of non-negative integers nums, the degree of this
#array is defined as the maximum frequency of any one of its elements.
#
#Your task is to find the smallest possible length of a (contiguous) subarray
#of nums, that has the same degree as nums.
#
#Example 1:
#Input: nums = [1,2,2,3,1]
#Output: 2
#Explanation: The input array has a degree of 2 because both elements 1 and 2
#appear twice. Of the subarrays that have the same degree:
#[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
#The shortest length is 2. So return 2.
#
#Example 2:
#Input: nums = [1,2,2,3,1,4,2]
#Output: 6
#Explanation: The degree is 3 because element 2 appears 3 times.
#The shortest subarray with degree 3 is [2,2,3,1,4,2] with length 6.
#
#Constraints:
#    nums.length will be between 1 and 50,000.
#    nums[i] will be an integer between 0 and 49,999.

from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """
        Track first/last occurrence and count for each element.
        Find elements with max count, return min span.
        """
        first = {}  # First occurrence index
        last = {}   # Last occurrence index
        count = {}  # Frequency count

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        min_length = len(nums)

        for num, freq in count.items():
            if freq == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)

        return min_length


class SolutionOnePass:
    """Single pass with simultaneous tracking"""

    def findShortestSubArray(self, nums: list[int]) -> int:
        first = {}
        count = {}
        degree = 0
        min_length = 0

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            count[num] = count.get(num, 0) + 1

            if count[num] > degree:
                degree = count[num]
                min_length = i - first[num] + 1
            elif count[num] == degree:
                min_length = min(min_length, i - first[num] + 1)

        return min_length


class SolutionCompact:
    """Compact version using defaultdict"""

    def findShortestSubArray(self, nums: list[int]) -> int:
        from collections import defaultdict

        left = {}
        right = {}
        count = defaultdict(int)

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1

        degree = max(count.values())

        return min(right[num] - left[num] + 1
                   for num in count
                   if count[num] == degree)
