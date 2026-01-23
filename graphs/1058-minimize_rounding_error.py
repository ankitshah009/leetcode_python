#1058. Minimize Rounding Error to Meet Target
#Medium
#
#Given an array of prices [p1,p2...,pn] and a target, round each price pi to
#Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)]
#sums to the given target. Each operation Roundi(pi) could be either
#Floor(pi) or Ceil(pi).
#
#Return the string "-1" if the rounded array is impossible to sum to target.
#Otherwise, return the smallest rounding error, which is defined as
#Σ|Roundi(pi) - pi| for i = 1 to n, as a string with three decimal places.
#
#Example 1:
#Input: prices = ["0.700","2.800","4.900"], target = 8
#Output: "1.000"
#Explanation: Use Floor, Ceil and Ceil operations to get 0 + 3 + 5 = 8.
#(0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0
#
#Example 2:
#Input: prices = ["1.500","2.500","3.500"], target = 10
#Output: "-1"
#Explanation: It is impossible to meet the target.
#
#Example 3:
#Input: prices = ["1.500","2.500","3.500"], target = 9
#Output: "1.500"
#
#Constraints:
#    1 <= prices.length <= 500
#    Each string prices[i] represents a real number in the range [0.0, 1000.0]
#    and has exactly 3 decimal places.
#    0 <= target <= 10^6

from typing import List
import math

class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        """
        For each price, compute floor and ceil errors.
        If price is integer, must use that (no choice).

        Min sum is sum of floors, max sum is sum of ceils.
        If target not in [min, max], return "-1".

        Greedily choose ceil for items with smallest ceil_error - floor_error.
        """
        floors = []
        ceils = []
        errors = []  # (ceil_error - floor_error, idx)

        for i, p in enumerate(prices):
            price = float(p)
            f = math.floor(price)
            c = math.ceil(price)

            floors.append(f)
            ceils.append(c)

            if f != c:  # Not an integer
                floor_error = price - f
                ceil_error = c - price
                errors.append((ceil_error - floor_error, i))

        min_sum = sum(floors)
        max_sum = sum(ceils)

        if target < min_sum or target > max_sum:
            return "-1"

        # Need to ceil (target - min_sum) items
        num_ceils = target - min_sum

        # Sort by how much better ceil is vs floor (smaller = prefer ceil)
        errors.sort()

        total_error = 0.0

        # Use ceil for first num_ceils items with choices
        ceil_idx = set()
        for i in range(num_ceils):
            _, idx = errors[i]
            ceil_idx.add(idx)

        for i, p in enumerate(prices):
            price = float(p)
            if i in ceil_idx:
                total_error += ceils[i] - price
            else:
                total_error += price - floors[i]

        return f"{total_error:.3f}"


class SolutionDP:
    def minimizeError(self, prices: List[str], target: int) -> str:
        """DP approach"""
        n = len(prices)
        INF = float('inf')

        floors = []
        diffs = []  # ceil - floor for each

        for p in prices:
            price = float(p)
            f = math.floor(price)
            c = math.ceil(price)
            floors.append(f)
            if f == c:
                diffs.append(None)  # Must use this value
            else:
                diffs.append(c - f)  # Always 1 for non-integers

        # dp[i] = min error to achieve sum i using first j items
        current_sum = sum(floors)
        if target < current_sum:
            return "-1"

        # Calculate min/max achievable
        max_extra = sum(1 for d in diffs if d is not None)
        if target > current_sum + max_extra:
            return "-1"

        num_ceils_needed = target - current_sum

        # Collect ceil errors for items with choice
        ceil_errors = []
        base_error = 0.0

        for i, p in enumerate(prices):
            price = float(p)
            if diffs[i] is None:
                base_error += 0  # Integer, no error
            else:
                floor_error = price - floors[i]
                ceil_error = ceils[i] - price if (ceils := [math.ceil(float(p)) for p in prices]) else 0
                ceil_error = math.ceil(price) - price
                ceil_errors.append((ceil_error - floor_error, floor_error))

        ceil_errors.sort()

        total = base_error + sum(fe for _, fe in ceil_errors)  # Start with all floors

        # Switch to ceil for num_ceils_needed items
        for i in range(num_ceils_needed):
            diff, floor_error = ceil_errors[i]
            total += diff  # ceil_error - floor_error

        return f"{total:.3f}"
