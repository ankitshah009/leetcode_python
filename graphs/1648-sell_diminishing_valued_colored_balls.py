#1648. Sell Diminishing-Valued Colored Balls
#Medium
#
#You have an inventory of different colored balls, and there is a customer that
#wants orders balls of any color.
#
#The customer weirdly values the colored balls. Each colored ball's value is the
#number of balls of that color you currently have in your inventory. For example,
#if you currently have 6 yellow balls, the customer would pay 6 for the first
#yellow ball. After the transaction, there are only 5 yellow balls left, so the
#next yellow ball is then valued at 5.
#
#You are given an integer array inventory, where inventory[i] represents the
#number of balls of the ith color that you initially own. You are also given an
#integer orders, which represents the total number of balls that the customer
#wants. You can sell the balls in any order.
#
#Return the maximum total value that you can attain after selling orders colored
#balls. As the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: inventory = [2,5], orders = 4
#Output: 14
#Explanation: Sell 5, 4, 3, 2 = 14.
#
#Example 2:
#Input: inventory = [3,5], orders = 6
#Output: 19
#Explanation: Sell 5, 4, 3, 3, 2, 2 = 19.
#
#Example 3:
#Input: inventory = [2,8,4,10,6], orders = 20
#Output: 110
#
#Constraints:
#    1 <= inventory.length <= 10^5
#    1 <= inventory[i] <= 10^9
#    1 <= orders <= min(sum(inventory[i]), 10^9)

from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        Binary search for the threshold value.
        Sell all balls above threshold, then fill remaining with threshold balls.
        """
        MOD = 10**9 + 7

        def sum_range(high: int, low: int) -> int:
            """Sum of integers from low+1 to high inclusive."""
            # sum = (high + low + 1) * (high - low) / 2
            return (high + low + 1) * (high - low) // 2

        inventory.sort(reverse=True)

        # Binary search for threshold
        left, right = 0, max(inventory)

        while left < right:
            mid = (left + right + 1) // 2
            # Count balls we can sell above mid
            count = sum(max(0, x - mid) for x in inventory)
            if count <= orders:
                right = mid - 1
            else:
                left = mid

        threshold = left

        # Calculate total value
        total = 0
        remaining = orders

        for balls in inventory:
            if balls > threshold:
                # Sell all balls from balls down to threshold+1
                count = balls - threshold
                total += sum_range(balls, threshold)
                remaining -= count

        # Sell remaining balls at threshold value
        total += threshold * remaining

        return total % MOD


class SolutionHeap:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        Greedy with max-heap (TLE for large inputs but conceptually clear).
        """
        import heapq

        MOD = 10**9 + 7

        # Max-heap
        heap = [-x for x in inventory]
        heapq.heapify(heap)

        total = 0

        while orders > 0:
            highest = -heapq.heappop(heap)
            second = -heap[0] if heap else 0

            # How many balls at this level
            count_at_level = 1

            # Collect all balls at same level
            while heap and -heap[0] == highest:
                heapq.heappop(heap)
                count_at_level += 1

            # Sell from highest down to second+1
            levels = highest - second
            total_balls = levels * count_at_level

            if total_balls <= orders:
                # Sell all
                # Sum: count_at_level * (highest + highest-1 + ... + second+1)
                total += count_at_level * (highest + second + 1) * levels // 2
                orders -= total_balls

                if second > 0:
                    for _ in range(count_at_level):
                        heapq.heappush(heap, -second)
            else:
                # Partial sell
                full_levels = orders // count_at_level
                extra = orders % count_at_level

                if full_levels > 0:
                    low = highest - full_levels + 1
                    total += count_at_level * (highest + low) * full_levels // 2

                total += extra * (highest - full_levels)
                orders = 0

        return total % MOD


class SolutionOptimized:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        Optimized with sorting and level processing.
        """
        MOD = 10**9 + 7

        inventory.sort(reverse=True)
        inventory.append(0)  # Sentinel

        total = 0
        width = 1

        for i in range(len(inventory) - 1):
            if inventory[i] > inventory[i + 1]:
                height = inventory[i] - inventory[i + 1]
                balls = height * width

                if balls <= orders:
                    # Sell all balls in this band
                    # Sum: width * (inventory[i] + inventory[i]+1 + ... + inventory[i+1]+1)
                    total += width * (inventory[i] + inventory[i + 1] + 1) * height // 2
                    orders -= balls
                else:
                    # Partial sell
                    full_rows = orders // width
                    leftover = orders % width

                    if full_rows > 0:
                        high = inventory[i]
                        low = inventory[i] - full_rows + 1
                        total += width * (high + low) * full_rows // 2

                    total += leftover * (inventory[i] - full_rows)
                    return total % MOD

            width += 1

        return total % MOD
