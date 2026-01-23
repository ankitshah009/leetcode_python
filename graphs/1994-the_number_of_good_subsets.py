#1994. The Number of Good Subsets
#Hard
#
#You are given an integer array nums. We call a subset of nums good if its
#product can be represented as a product of one or more distinct prime numbers.
#
#For example, if nums = [1, 2, 3, 4]:
#- [2, 3], [1, 2, 3], [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3,
#  3 = 3 respectively.
#- [1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2
#  respectively.
#
#Return the number of different good subsets in nums modulo 10^9 + 7.
#
#A subset of nums is any array that can be obtained by deleting some (possibly
#none or all) elements from nums. Two subsets are different if and only if the
#chosen indices to delete are different.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: 6
#Explanation: The good subsets are: [1,2], [1,3], [2], [1,2,3], [2,3], [3].
#
#Example 2:
#Input: nums = [4,2,3,15]
#Output: 5
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 30

from typing import List
from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        """
        Bitmask DP where each prime maps to a bit.
        Numbers with repeated prime factors (4, 8, 9, etc.) are excluded.
        """
        MOD = 10**9 + 7

        # Primes up to 30
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_to_idx = {p: i for i, p in enumerate(primes)}

        # Map each valid number (2-30) to its prime mask
        def get_mask(n: int) -> int:
            """Returns bitmask of prime factors, or -1 if has repeated factors."""
            if n == 1:
                return 0

            mask = 0
            for i, p in enumerate(primes):
                if n % p == 0:
                    n //= p
                    if n % p == 0:  # Repeated prime factor
                        return -1
                    mask |= (1 << i)

            return mask if n == 1 else -1

        # Precompute masks for all numbers 1-30
        masks = {i: get_mask(i) for i in range(1, 31)}

        # Count occurrences
        count = Counter(nums)

        # DP: dp[mask] = number of ways to achieve this prime mask
        dp = [0] * (1 << len(primes))
        dp[0] = 1

        for num in range(2, 31):
            if num not in count or masks[num] == -1:
                continue

            mask = masks[num]
            cnt = count[num]

            # Update DP in reverse to avoid using same number twice
            for prev_mask in range((1 << len(primes)) - 1, -1, -1):
                if dp[prev_mask] and (prev_mask & mask) == 0:
                    new_mask = prev_mask | mask
                    dp[new_mask] = (dp[new_mask] + dp[prev_mask] * cnt) % MOD

        # Sum all non-empty subsets
        result = sum(dp[1:]) % MOD

        # Multiply by 2^count[1] (each 1 can be included or not)
        ones = count.get(1, 0)
        result = (result * pow(2, ones, MOD)) % MOD

        return result


class SolutionExplained:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        """
        Detailed approach with comments.
        """
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        # Numbers that can be in good subsets (no repeated prime factors)
        valid = {2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30}

        def prime_mask(n):
            mask = 0
            for i, p in enumerate(primes):
                if n % p == 0:
                    mask |= (1 << i)
            return mask

        count = Counter(nums)

        # dp[mask] = ways to form subset with prime mask
        dp = {0: 1}

        for num in valid:
            if num not in count:
                continue

            mask = prime_mask(num)
            cnt = count[num]

            new_dp = dp.copy()

            for prev_mask, ways in dp.items():
                if (prev_mask & mask) == 0:  # No overlap
                    new_mask = prev_mask | mask
                    new_dp[new_mask] = (new_dp.get(new_mask, 0) + ways * cnt) % MOD

            dp = new_dp

        # Total (excluding empty subset)
        result = (sum(dp.values()) - 1) % MOD

        # Multiply by 2^(count of 1s)
        result = (result * pow(2, count.get(1, 0), MOD)) % MOD

        return result
