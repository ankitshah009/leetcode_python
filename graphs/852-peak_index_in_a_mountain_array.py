#852. Peak Index in a Mountain Array
#Medium
#
#An array arr a mountain if the following properties hold:
#- arr.length >= 3
#- There exists some i with 0 < i < arr.length - 1 such that:
#  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#Given a mountain array arr, return the index i such that arr[0] < arr[1] < ...
#< arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
#
#You must solve it in O(log(arr.length)) time complexity.
#
#Example 1:
#Input: arr = [0,1,0]
#Output: 1
#
#Example 2:
#Input: arr = [0,2,1,0]
#Output: 1
#
#Example 3:
#Input: arr = [0,10,5,2]
#Output: 1
#
#Constraints:
#    3 <= arr.length <= 10^5
#    0 <= arr[i] <= 10^6
#    arr is guaranteed to be a mountain array.

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        """
        Binary search: if arr[mid] < arr[mid+1], peak is to the right.
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionLinear:
    """O(n) solution - find where increase stops"""

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return i - 1
        return len(arr) - 1


class SolutionMax:
    """Using built-in max - O(n)"""

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return arr.index(max(arr))


class SolutionTernarySearch:
    """Ternary search for unimodal function"""

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        while right - left > 2:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            if arr[mid1] < arr[mid2]:
                left = mid1
            else:
                right = mid2

        # Find max in remaining range
        return max(range(left, right + 1), key=lambda i: arr[i])
