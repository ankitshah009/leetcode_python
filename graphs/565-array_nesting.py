#565. Array Nesting
#Medium
#
#You are given an integer array nums of length n where nums is a permutation of
#the numbers in the range [0, n - 1].
#
#You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... }
#subjected to the following rule:
#
#The first element in s[k] starts with the selection of the element nums[k] of index k.
#The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], etc.
#We stop adding right before a duplicate element occurs in s[k].
#
#Return the longest length of a set s[k].
#
#Example 1:
#Input: nums = [5,4,0,3,1,6,2]
#Output: 4
#Explanation: nums[0] = 5, nums[5] = 6, nums[6] = 2, nums[2] = 0.
#So s[0] = {5, 6, 2, 0}
#
#Example 2:
#Input: nums = [0,1,2]
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] < nums.length
#    All the values of nums are unique.

from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Array forms disjoint cycles.
        Find longest cycle without revisiting.
        """
        max_len = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i]:
                continue

            length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = nums[j]
                length += 1

            max_len = max(max_len, length)

        return max_len


class SolutionMark:
    """Mark visited by modifying array"""

    def arrayNesting(self, nums: List[int]) -> int:
        max_len = 0
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                continue

            length = 0
            j = i

            while nums[j] >= 0:
                next_j = nums[j]
                nums[j] = -1  # Mark as visited
                j = next_j
                length += 1

            max_len = max(max_len, length)

        return max_len


class SolutionSet:
    """Using set for visited tracking"""

    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        max_len = 0

        for i in range(len(nums)):
            if i in visited:
                continue

            length = 0
            j = i

            while j not in visited:
                visited.add(j)
                j = nums[j]
                length += 1

            max_len = max(max_len, length)

        return max_len
