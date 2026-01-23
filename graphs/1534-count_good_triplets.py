#1534. Count Good Triplets
#Easy
#
#Given an array of integers arr, and three integers a, b and c. You need to find
#the number of good triplets.
#
#A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#- 0 <= i < j < k < arr.length
#- |arr[i] - arr[j]| <= a
#- |arr[j] - arr[k]| <= b
#- |arr[i] - arr[k]| <= c
#
#Where |x| denotes the absolute value of x.
#
#Return the number of good triplets.
#
#Example 1:
#Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
#Output: 4
#Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
#
#Example 2:
#Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
#Output: 0
#Explanation: No triplet satisfies all conditions.
#
#Constraints:
#    3 <= arr.length <= 100
#    0 <= arr[i] <= 1000
#    0 <= a, b, c <= 1000

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Brute force with early pruning.
        Check all triplets (i, j, k) where i < j < k.
        """
        n = len(arr)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # Check first condition early
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, n):
                    if (abs(arr[j] - arr[k]) <= b and
                        abs(arr[i] - arr[k]) <= c):
                        count += 1

        return count


class SolutionOptimized:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Enumerate j as the middle element, then count valid (i, k) pairs.
        """
        n = len(arr)
        count = 0

        for j in range(1, n - 1):
            # Find all valid i's (i < j, |arr[i] - arr[j]| <= a)
            valid_i = []
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    valid_i.append(arr[i])

            # Find all valid k's (k > j, |arr[j] - arr[k]| <= b)
            valid_k = []
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    valid_k.append(arr[k])

            # Count pairs (i, k) where |arr[i] - arr[k]| <= c
            for vi in valid_i:
                for vk in valid_k:
                    if abs(vi - vk) <= c:
                        count += 1

        return count


class SolutionComprehension:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Using list comprehension and sum.
        """
        n = len(arr)
        return sum(
            1
            for i in range(n)
            for j in range(i + 1, n)
            for k in range(j + 1, n)
            if (abs(arr[i] - arr[j]) <= a and
                abs(arr[j] - arr[k]) <= b and
                abs(arr[i] - arr[k]) <= c)
        )


class SolutionEnumerate:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Using enumerate for cleaner code.
        """
        count = 0

        for i, vi in enumerate(arr[:-2]):
            for j, vj in enumerate(arr[i + 1:-1], start=i + 1):
                if abs(vi - vj) <= a:
                    for vk in arr[j + 1:]:
                        if abs(vj - vk) <= b and abs(vi - vk) <= c:
                            count += 1

        return count
