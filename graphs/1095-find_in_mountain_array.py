#1095. Find in Mountain Array
#Hard
#
#You may recall that an array arr is a mountain array if and only if:
#    arr.length >= 3
#    There exists some i with 0 < i < arr.length - 1 such that:
#        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#Given a mountain array mountainArr, return the minimum index such that
#mountainArr.get(index) == target. If such an index does not exist, return -1.
#
#You cannot access the mountain array directly. You may only access the array
#using a MountainArray interface:
#    MountainArray.get(k) returns the element of the array at index k (0-indexed).
#    MountainArray.length() returns the length of the array.
#
#Submissions making more than 100 calls to MountainArray.get will be judged
#Wrong Answer.
#
#Example 1:
#Input: array = [1,2,3,4,5,3,1], target = 3
#Output: 2
#
#Example 2:
#Input: array = [0,1,2,4,2,1], target = 3
#Output: -1
#
#Constraints:
#    3 <= mountain_arr.length() <= 10^4
#    0 <= target <= 10^9
#    0 <= mountain_arr.get(index) <= 10^9

# This is MountainArray's API interface.
class MountainArray:
    def get(self, index: int) -> int:
        pass
    def length(self) -> int:
        pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
        1. Binary search to find peak
        2. Binary search in ascending part
        3. Binary search in descending part
        """
        n = mountain_arr.length()

        # Find peak
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # Binary search in ascending part
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search in descending part
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class SolutionCached:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """Cache get() calls to minimize API usage"""
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountain_arr.get(i)
            return cache[i]

        n = mountain_arr.length()

        # Find peak
        lo, hi = 1, n - 2
        while lo < hi:
            mid = (lo + hi) // 2
            if get(mid) < get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        # Search ascending side
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = get(mid)
            if val == target:
                return mid
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # Search descending side
        lo, hi = peak, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = get(mid)
            if val == target:
                return mid
            if val > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
