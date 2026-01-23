#1243. Array Transformation
#Easy
#
#Given an initial array arr, every day you produce a new array using the array
#of the previous day.
#
#On the i-th day, you do the following operations on the array of day i-1 to
#produce the array of day i:
#    If an element is smaller than both its left neighbor and its right neighbor,
#    then this element is incremented.
#    If an element is bigger than both its left neighbor and its right neighbor,
#    then this element is decremented.
#    The first and last elements never change.
#
#After some days, the array does not change. Return that final array.
#
#Example 1:
#Input: arr = [6,2,3,4]
#Output: [6,3,3,4]
#Explanation:
#On day 1: [6,2,3,4] -> [6,3,3,4]
#On day 2: [6,3,3,4] -> [6,3,3,4] (no change)
#
#Example 2:
#Input: arr = [1,6,3,4,3,5]
#Output: [1,4,4,4,4,5]
#
#Constraints:
#    3 <= arr.length <= 100
#    1 <= arr[i] <= 100

from typing import List

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        """
        Simulate until no changes.
        """
        changed = True

        while changed:
            changed = False
            new_arr = arr.copy()

            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new_arr[i] = arr[i] + 1
                    changed = True
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new_arr[i] = arr[i] - 1
                    changed = True

            arr = new_arr

        return arr


class SolutionExplicit:
    def transformArray(self, arr: List[int]) -> List[int]:
        """More explicit simulation"""
        n = len(arr)

        while True:
            modifications = []

            for i in range(1, n - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    modifications.append((i, 1))  # Increment
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    modifications.append((i, -1))  # Decrement

            if not modifications:
                break

            for idx, delta in modifications:
                arr[idx] += delta

        return arr
