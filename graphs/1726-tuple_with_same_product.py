#1726. Tuple with Same Product
#Medium
#
#Given an array nums of distinct positive integers, return the number of tuples
#(a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums,
#and a != b != c != d.
#
#Example 1:
#Input: nums = [2,3,4,6]
#Output: 8
#
#Example 2:
#Input: nums = [1,2,4,5,10]
#Output: 16
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 10^4
#    All elements in nums are distinct.

from typing import List
from collections import Counter

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Count pairs with same product.
        For each product appearing k times, we can form k*(k-1)/2 pair combinations.
        Each pair combination gives 8 tuples (2 ways to order each pair, 2 ways to swap pairs).
        """
        product_count = Counter()

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product_count[nums[i] * nums[j]] += 1

        result = 0
        for count in product_count.values():
            if count >= 2:
                # C(count, 2) = count * (count - 1) / 2 pairs
                # Each pair of pairs gives 8 tuples
                result += count * (count - 1) // 2 * 8

        return result


class SolutionDetailed:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Same approach with detailed explanation.
        """
        from collections import defaultdict

        # Map: product -> list of (i, j) pairs
        product_pairs = defaultdict(list)

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                product_pairs[prod].append((i, j))

        total = 0

        for pairs in product_pairs.values():
            k = len(pairs)
            if k < 2:
                continue

            # For each pair of pairs (a,b) and (c,d), we get 8 tuples:
            # (a,b,c,d), (a,b,d,c), (b,a,c,d), (b,a,d,c)
            # (c,d,a,b), (c,d,b,a), (d,c,a,b), (d,c,b,a)
            num_pair_combinations = k * (k - 1) // 2
            total += num_pair_combinations * 8

        return total
