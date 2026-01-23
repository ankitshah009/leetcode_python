#1390. Four Divisors
#Medium
#
#Given an integer array nums, return the sum of divisors of the integers in
#that array that have exactly four divisors. If there is no such integer in
#the array, return 0.
#
#Example 1:
#Input: nums = [21,4,7]
#Output: 32
#Explanation:
#21 has 4 divisors: 1, 3, 7, 21
#4 has 3 divisors: 1, 2, 4
#7 has 2 divisors: 1, 7
#The answer is the sum of divisors of 21 only = 32
#
#Example 2:
#Input: nums = [21,21]
#Output: 64
#
#Example 3:
#Input: nums = [1,2,3,4,5]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^4
#    1 <= nums[i] <= 10^5

from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        For each number, find all divisors. If exactly 4, add their sum.
        Optimize: iterate up to sqrt(n) to find divisor pairs.
        """
        def get_divisors_sum_if_four(n: int) -> int:
            divisors = []

            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)

                    # Early termination if more than 4 divisors
                    if len(divisors) > 4:
                        return 0

            if len(divisors) == 4:
                return sum(divisors)
            return 0

        return sum(get_divisors_sum_if_four(num) for num in nums)


class SolutionExplicit:
    def sumFourDivisors(self, nums: List[int]) -> int:
        """More explicit approach"""
        total = 0

        for num in nums:
            divisors = []
            sqrt_num = int(math.sqrt(num))

            for i in range(1, sqrt_num + 1):
                if num % i == 0:
                    divisors.append(i)
                    if i * i != num:
                        divisors.append(num // i)

            if len(divisors) == 4:
                total += sum(divisors)

        return total


class SolutionWithCache:
    def sumFourDivisors(self, nums: List[int]) -> int:
        """Cache results for repeated numbers"""
        cache = {}

        def get_divisors_sum_if_four(n: int) -> int:
            if n in cache:
                return cache[n]

            divisor_sum = 0
            count = 0

            i = 1
            while i * i <= n:
                if n % i == 0:
                    count += 1
                    divisor_sum += i

                    if i * i != n:
                        count += 1
                        divisor_sum += n // i

                    if count > 4:
                        cache[n] = 0
                        return 0
                i += 1

            result = divisor_sum if count == 4 else 0
            cache[n] = result
            return result

        return sum(get_divisors_sum_if_four(num) for num in nums)
