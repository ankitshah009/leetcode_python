#1619. Mean of Array After Removing Some Elements
#Easy
#
#Given an integer array arr, return the mean of the remaining integers after
#removing the smallest 5% and the largest 5% of the elements.
#
#Answers within 10^-5 of the actual answer will be considered accepted.
#
#Example 1:
#Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
#Output: 2.00000
#Explanation: After erasing the minimum and the maximum values of this array,
#all elements are equal to 2, so the mean is 2.
#
#Example 2:
#Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
#Output: 4.00000
#
#Example 3:
#Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
#Output: 4.77778
#
#Constraints:
#    20 <= arr.length <= 1000
#    arr.length is a multiple of 20.
#    0 <= arr[i] <= 10^5

from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """
        Sort, remove 5% from each end, compute mean.
        """
        arr.sort()
        n = len(arr)
        remove = n // 20  # 5% = n/20

        # Keep elements from index 'remove' to 'n - remove - 1'
        trimmed = arr[remove:n - remove]

        return sum(trimmed) / len(trimmed)


class SolutionManual:
    def trimMean(self, arr: List[int]) -> float:
        """
        Manual calculation without slicing.
        """
        arr.sort()
        n = len(arr)
        five_percent = n // 20

        total = 0
        count = 0

        for i in range(five_percent, n - five_percent):
            total += arr[i]
            count += 1

        return total / count


class SolutionStatistics:
    def trimMean(self, arr: List[int]) -> float:
        """
        Using statistics module (conceptually).
        """
        from statistics import mean

        arr.sort()
        n = len(arr)
        trim = n // 20

        return mean(arr[trim:n - trim])


class SolutionHeap:
    def trimMean(self, arr: List[int]) -> float:
        """
        Using heaps to find trimmed elements (less efficient but different).
        """
        import heapq

        n = len(arr)
        trim = n // 20

        # Get smallest 5% to exclude
        smallest = heapq.nsmallest(trim, arr)
        # Get largest 5% to exclude
        largest = heapq.nlargest(trim, arr)

        total = sum(arr) - sum(smallest) - sum(largest)
        count = n - 2 * trim

        return total / count
