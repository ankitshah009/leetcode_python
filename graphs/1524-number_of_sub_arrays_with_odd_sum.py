#1524. Number of Sub-arrays With Odd Sum
#Medium
#
#Given an array of integers arr, return the number of subarrays with an odd sum.
#
#Since the answer can be very large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: arr = [1,3,5]
#Output: 4
#Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
#All sub-arrays sum are [1,4,9,3,8,5].
#Odd sums are [1,9,3,5] so the answer is 4.
#
#Example 2:
#Input: arr = [2,4,6]
#Output: 0
#Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
#All sub-arrays sum are [2,6,12,4,10,6].
#All sub-arrays have even sum and the answer is 0.
#
#Example 3:
#Input: arr = [1,2,3,4,5,6,7]
#Output: 16
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= arr[i] <= 100

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Track count of odd and even prefix sums.
        Subarray sum = prefix[j] - prefix[i-1] is odd when parities differ.
        """
        MOD = 10**9 + 7

        odd_count = 0  # Count of prefix sums with odd parity
        even_count = 1  # Count of prefix sums with even parity (include 0)

        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 1:
                # Current prefix is odd
                # Odd sum subarrays: pair with even prefix sums
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # Current prefix is even
                # Odd sum subarrays: pair with odd prefix sums
                result = (result + odd_count) % MOD
                even_count += 1

        return result


class SolutionAlternative:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Alternative: track only the parity of prefix sum.
        """
        MOD = 10**9 + 7

        # count[0] = even prefix sums, count[1] = odd prefix sums
        count = [1, 0]  # Start with one even (empty prefix = 0)

        parity = 0  # Current prefix sum parity
        result = 0

        for num in arr:
            parity = (parity + num) % 2

            # Number of subarrays ending here with odd sum
            result = (result + count[1 - parity]) % MOD

            count[parity] += 1

        return result


class SolutionDP:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        DP approach: odd[i] = subarrays ending at i with odd sum
                     even[i] = subarrays ending at i with even sum
        """
        MOD = 10**9 + 7
        n = len(arr)

        odd = 0  # Odd sum subarrays ending at current position
        even = 0  # Even sum subarrays ending at current position

        result = 0

        for num in arr:
            if num % 2 == 1:
                # Odd number: odd -> even, even -> odd
                odd, even = even + 1, odd
            else:
                # Even number: parities stay same
                even = even + 1

            result = (result + odd) % MOD

        return result


class SolutionCounting:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Count odd prefix sums and use combinatorics.
        """
        MOD = 10**9 + 7

        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        # Count odd and even prefix sums
        odd = sum(1 for p in prefix if p % 2 == 1)
        even = len(prefix) - odd

        # Subarrays with odd sum = odd * even
        return (odd * even) % MOD
