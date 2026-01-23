#702. Search in a Sorted Array of Unknown Size
#Medium
#
#This is an interactive problem.
#
#You have a sorted array of unique elements and an unknown size. You do not have
#an access to the array but you can use the ArrayReader interface to access it.
#You can call ArrayReader.get(i) that:
#- returns the value at the ith index (0-indexed) of the secret array, or
#- returns 2^31 - 1 if the i is out of the boundary of the array.
#
#You are also given an integer target.
#
#Return the index k of the hidden array where secret[k] == target or return -1
#otherwise.
#
#You must write an algorithm with O(log n) runtime complexity.
#
#Example 1:
#Input: secret = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in secret and its index is 4.
#
#Example 2:
#Input: secret = [-1,0,3,5,9,12], target = 2
#Output: -1
#Explanation: 2 does not exist in secret so return -1.
#
#Constraints:
#    1 <= secret.length <= 10^4
#    -10^4 <= secret[i], target <= 10^4
#    secret is sorted in a strictly increasing order.

# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target: int) -> int:
        """
        1. Find the search boundary by exponential search
        2. Binary search within that boundary
        """
        # Find the right boundary
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2

        # Binary search
        while left <= right:
            mid = left + (right - left) // 2
            val = reader.get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class SolutionDetailed:
    """More explicit boundary finding"""

    def search(self, reader, target: int) -> int:
        OUT_OF_BOUNDS = 2147483647  # 2^31 - 1

        # First, find a valid upper bound
        bound = 1
        while reader.get(bound) < target and reader.get(bound) != OUT_OF_BOUNDS:
            bound *= 2

        # Binary search between bound/2 and bound
        left, right = bound // 2, bound

        while left <= right:
            mid = left + (right - left) // 2
            val = reader.get(mid)

            if val == target:
                return mid
            elif val == OUT_OF_BOUNDS or val > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
