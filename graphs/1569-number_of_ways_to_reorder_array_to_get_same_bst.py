#1569. Number of Ways to Reorder Array to Get Same BST
#Hard
#
#Given an array nums that represents a permutation of integers from 1 to n. We
#are going to construct a binary search tree (BST) by inserting the elements of
#nums in order into an initially empty BST. Find the number of different ways to
#reorder nums so that the constructed BST is identical to that formed from the
#original array nums.
#
#For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child,
#and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1]
#yields a different BST.
#
#Return the number of ways to reorder nums such that the BST formed is identical
#to the original BST formed from nums.
#
#Since the answer may be very large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums = [2,1,3]
#Output: 1
#Explanation: We can reorder nums to be [2,3,1] which will yield the same BST.
#There are no other ways to reorder nums which will yield the same BST.
#
#Example 2:
#Input: nums = [3,4,5,1,2]
#Output: 5
#Explanation: The following 5 arrays will yield the same BST:
#[3,1,2,4,5]
#[3,1,4,2,5]
#[3,1,4,5,2]
#[3,4,1,2,5]
#[3,4,1,5,2]
#
#Example 3:
#Input: nums = [1,2,3]
#Output: 0
#Explanation: There are no other orderings of nums that will yield the same BST.
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= nums.length
#    All integers in nums are distinct.

from typing import List
from functools import lru_cache
from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        """
        Recursive approach using combinatorics.

        For a BST with root r:
        - Left subtree contains elements < r
        - Right subtree contains elements > r
        - We can interleave left and right elements in C(left+right, left) ways
        - Multiply by ways to reorder each subtree
        """
        MOD = 10**9 + 7

        def count_ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            # Ways to interleave left and right while maintaining relative order
            ways = comb(len(left) + len(right), len(left)) % MOD

            # Multiply by ways to arrange each subtree
            ways = (ways * count_ways(left)) % MOD
            ways = (ways * count_ways(right)) % MOD

            return ways

        # Subtract 1 because we don't count the original ordering
        return (count_ways(nums) - 1) % MOD


class SolutionPascal:
    def numOfWays(self, nums: List[int]) -> int:
        """
        Using Pascal's triangle for combinations to avoid overflow.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute Pascal's triangle
        pascal = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                pascal[i][j] = (pascal[i-1][j-1] + pascal[i-1][j]) % MOD

        def count(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = count(left)
            right_ways = count(right)

            # C(left + right, left) * left_ways * right_ways
            return (pascal[len(left) + len(right)][len(left)] *
                    left_ways % MOD * right_ways) % MOD

        return (count(nums) - 1) % MOD


class SolutionModInverse:
    def numOfWays(self, nums: List[int]) -> int:
        """
        Using modular inverse for combinations.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        def count(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            return (nCr(len(left) + len(right), len(left)) *
                    count(left) % MOD * count(right)) % MOD

        return (count(nums) - 1) % MOD
