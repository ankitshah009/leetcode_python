#658. Find K Closest Elements
#Medium
#
#Given a sorted integer array arr, two integers k and x, return the k closest
#integers to x in the array. The result should also be sorted in ascending order.
#
#An integer a is closer to x than an integer b if:
#- |a - x| < |b - x|, or
#- |a - x| == |b - x| and a < b
#
#Example 1:
#Input: arr = [1,2,3,4,5], k = 4, x = 3
#Output: [1,2,3,4]
#
#Example 2:
#Input: arr = [1,2,3,4,5], k = 4, x = -1
#Output: [1,2,3,4]
#
#Constraints:
#    1 <= k <= arr.length
#    1 <= arr.length <= 10^4
#    arr is sorted in ascending order.
#    -10^4 <= arr[i], x <= 10^4

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search to find the starting index of k elements.
        """
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2

            # Compare distance from arr[mid] to x vs arr[mid+k] to x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


class SolutionTwoPointers:
    """Two pointers shrinking window"""

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left:right + 1]


class SolutionHeap:
    """Max heap approach"""

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq

        # Max heap with (negative_distance, negative_value, value)
        heap = []

        for num in arr:
            dist = abs(num - x)

            if len(heap) < k:
                heapq.heappush(heap, (-dist, -num, num))
            elif -dist > heap[0][0] or (-dist == heap[0][0] and -num > heap[0][1]):
                heapq.heapreplace(heap, (-dist, -num, num))

        return sorted(item[2] for item in heap)


class SolutionBisect:
    """Using bisect for insertion point"""

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import bisect

        # Find insertion point
        pos = bisect.bisect_left(arr, x)
        left, right = pos - 1, pos

        result = []

        while len(result) < k:
            if left < 0:
                result.append(arr[right])
                right += 1
            elif right >= len(arr):
                result.append(arr[left])
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1

        return sorted(result)
