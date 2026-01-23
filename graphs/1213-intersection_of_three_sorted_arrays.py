#1213. Intersection of Three Sorted Arrays
#Easy
#
#Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing
#order, return a sorted array of only the integers that appeared in all three arrays.
#
#Example 1:
#Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
#Output: [1,5]
#Explanation: Only 1 and 5 appeared in the three arrays.
#
#Example 2:
#Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
#Output: []
#
#Constraints:
#    1 <= arr1.length, arr2.length, arr3.length <= 1000
#    1 <= arr1[i], arr2[i], arr3[i] <= 2000

from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """Three pointers approach"""
        i = j = k = 0
        result = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                i += 1
            elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1

        return result


class SolutionSet:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """Using set intersection"""
        common = set(arr1) & set(arr2) & set(arr3)
        return sorted(common)


class SolutionCounter:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """Count occurrences"""
        from collections import Counter

        count = Counter(arr1 + arr2 + arr3)
        return [num for num in arr1 if count[num] == 3]
