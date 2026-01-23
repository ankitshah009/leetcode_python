#1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
#Medium
#
#Given two arrays of integers nums1 and nums2, return the number of triplets
#formed (type 1 and type 2) under the following rules:
#
#Type 1: Triplet (i, j, k) if nums1[i]^2 == nums2[j] * nums2[k] where
#0 <= i < nums1.length and 0 <= j < k < nums2.length.
#
#Type 2: Triplet (i, j, k) if nums2[i]^2 == nums1[j] * nums1[k] where
#0 <= i < nums2.length and 0 <= j < k < nums1.length.
#
#Example 1:
#Input: nums1 = [7,4], nums2 = [5,2,8,9]
#Output: 1
#Explanation: Type 1: (1, 1, 2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8).
#
#Example 2:
#Input: nums1 = [1,1], nums2 = [1,1,1]
#Output: 9
#Explanation: All Triplets are valid, because 1^2 = 1 * 1.
#Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2). nums1[i]^2 = nums2[j] * nums2[k].
#Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
#
#Example 3:
#Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
#Output: 2
#Explanation: There are 2 valid triplets.
#Type 1: (3,0,2). nums1[3]^2 = nums2[0] * nums2[2]. (3^2 = 1 * 9).
#Type 2: (3,0,1). nums2[3]^2 = nums1[0] * nums1[1]. (7^2 = 7 * 7).
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 1000
#    1 <= nums1[i], nums2[i] <= 10^5

from typing import List
from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Count triplets of both types using hash map.
        """
        def count_triplets(squares: List[int], products: List[int]) -> int:
            """Count triplets where squares[i]^2 == products[j] * products[k]"""
            count = 0
            prod_count = Counter()

            # For each pair in products, count products
            for j in range(len(products)):
                for k in range(j + 1, len(products)):
                    prod_count[products[j] * products[k]] += 1

            # Check each square
            for num in squares:
                target = num * num
                count += prod_count[target]

            return count

        type1 = count_triplets(nums1, nums2)
        type2 = count_triplets(nums2, nums1)

        return type1 + type2


class SolutionOptimized:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Optimized: Use two-sum style approach for each square.
        """
        def count_pairs(arr: List[int], target: int) -> int:
            """Count pairs (j, k) where j < k and arr[j] * arr[k] == target"""
            if target == 0:
                return 0

            count = 0
            seen = Counter()

            for num in arr:
                if target % num == 0:
                    count += seen[target // num]
                seen[num] += 1

            return count

        result = 0

        # Type 1: nums1[i]^2 == nums2[j] * nums2[k]
        for num in nums1:
            result += count_pairs(nums2, num * num)

        # Type 2: nums2[i]^2 == nums1[j] * nums1[k]
        for num in nums2:
            result += count_pairs(nums1, num * num)

        return result


class SolutionBruteForce:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Brute force O(n * m^2) approach.
        """
        count = 0

        # Type 1
        for i in range(len(nums1)):
            sq = nums1[i] * nums1[i]
            for j in range(len(nums2)):
                for k in range(j + 1, len(nums2)):
                    if nums2[j] * nums2[k] == sq:
                        count += 1

        # Type 2
        for i in range(len(nums2)):
            sq = nums2[i] * nums2[i]
            for j in range(len(nums1)):
                for k in range(j + 1, len(nums1)):
                    if nums1[j] * nums1[k] == sq:
                        count += 1

        return count


class SolutionHashMap:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Using hash maps for product counts.
        """
        def product_counts(arr):
            """Return Counter of all pair products"""
            cnt = Counter()
            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    cnt[arr[i] * arr[j]] += 1
            return cnt

        prod1 = product_counts(nums1)
        prod2 = product_counts(nums2)

        result = 0
        for num in nums1:
            result += prod2[num * num]
        for num in nums2:
            result += prod1[num * num]

        return result
