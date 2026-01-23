#1442. Count Triplets That Can Form Two Arrays of Equal XOR
#Medium
#
#Given an array of integers arr.
#
#We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
#
#Let's define a and b as follows:
#    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
#
#Note that ^ denotes the bitwise-xor operation.
#
#Return the number of triplets (i, j, k) Where a == b.
#
#Example 1:
#Input: arr = [2,3,1,6,7]
#Output: 4
#Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
#
#Example 2:
#Input: arr = [1,1,1,1,1]
#Output: 10
#
#Constraints:
#    1 <= arr.length <= 300
#    1 <= arr[i] <= 10^8

from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        a == b means a ^ b == 0
        a ^ b = arr[i] ^ ... ^ arr[k] = 0

        So we need to find pairs (i, k) where XOR of arr[i..k] = 0.
        For each such pair, j can be any value from i+1 to k.
        Number of valid j = k - i.

        Use prefix XOR: prefix[i] ^ prefix[k+1] = arr[i..k]
        So prefix[i] = prefix[k+1] means XOR = 0.
        """
        n = len(arr)

        # Compute prefix XOR
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        count = 0

        # For each pair (i, k) where prefix[i] == prefix[k+1]
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    # j can be i+1, i+2, ..., k (total k - i choices)
                    count += k - i

        return count


class SolutionOptimized:
    def countTriplets(self, arr: List[int]) -> int:
        """
        O(n) solution using hash map.
        For each prefix XOR value, track count and sum of indices.
        """
        n = len(arr)
        prefix = 0
        count = 0

        # Map from XOR value to (count, sum of indices)
        xor_count = defaultdict(int)
        xor_index_sum = defaultdict(int)

        xor_count[0] = 1
        xor_index_sum[0] = 0  # Index -1 + 1 = 0

        for k in range(n):
            prefix ^= arr[k]

            # For all i where prefix[i] == prefix[k+1]
            # Contribution is sum of (k - i) = count * k - sum_of_i
            if prefix in xor_count:
                count += xor_count[prefix] * k - xor_index_sum[prefix]

            xor_count[prefix] += 1
            xor_index_sum[prefix] += k + 1  # Store k+1 as "index" for next iteration

        return count


class SolutionBruteForce:
    def countTriplets(self, arr: List[int]) -> int:
        """O(n^3) brute force for comparison"""
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    # Calculate a and b
                    a = 0
                    for idx in range(i, j):
                        a ^= arr[idx]

                    b = 0
                    for idx in range(j, k + 1):
                        b ^= arr[idx]

                    if a == b:
                        count += 1

        return count
