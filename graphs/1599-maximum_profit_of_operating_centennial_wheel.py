#1599. Maximum Profit of Operating a Centennial Wheel
#Medium
#
#You are the operator of a Centennial Wheel that has four gondolas, and each
#gondola has room for up to four people. You have the ability to rotate the
#gondolas counterclockwise, which costs you runningCost dollars.
#
#You are given an array customers of length n where customers[i] is the number
#of new customers arriving just before the ith rotation (0-indexed). This means
#you must rotate the wheel i times before the customers[i] customers arrive.
#You cannot make customers wait if there is room in the gondola. Each customer
#pays boardingCost dollars when they board the gondola closest to the ground.
#
#You can stop the wheel at any time, including before serving all customers.
#If you decide to stop serving customers, all subsequent rotations are free.
#Return the minimum number of rotations you need to perform to maximize profit.
#If there is no scenario in which the profit is positive, return -1.
#
#Example 1:
#Input: customers = [8,3], boardingCost = 5, runningCost = 6
#Output: 3
#Explanation: After rotation 1: 4 board, 4 wait, profit = 4*5-6 = 14.
#After rotation 2: 4 board, 3 wait, profit = 8*5-12 = 28.
#After rotation 3: 3 board, 0 wait, profit = 11*5-18 = 37.
#
#Example 2:
#Input: customers = [10,9,6], boardingCost = 6, runningCost = 4
#Output: 7
#
#Example 3:
#Input: customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92
#Output: -1
#Explanation: Running cost is too high to ever make profit.
#
#Constraints:
#    n == customers.length
#    1 <= n <= 10^5
#    0 <= customers[i] <= 50
#    1 <= boardingCost, runningCost <= 100

from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        """
        Simulate the wheel rotation.
        Track maximum profit and the rotation number where it occurs.
        """
        waiting = 0
        profit = 0
        max_profit = 0
        best_rotation = -1
        rotation = 0

        i = 0
        n = len(customers)

        while i < n or waiting > 0:
            # Add new customers if available
            if i < n:
                waiting += customers[i]
                i += 1

            # Board up to 4 customers
            board = min(4, waiting)
            waiting -= board

            # Update profit
            rotation += 1
            profit += board * boardingCost - runningCost

            # Track best
            if profit > max_profit:
                max_profit = profit
                best_rotation = rotation

        return best_rotation


class SolutionOptimized:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        """
        Optimized: After processing all arrival times, calculate remaining
        rotations mathematically.
        """
        waiting = 0
        profit = 0
        max_profit = 0
        best_rotation = -1
        rotation = 0

        # Process arrivals
        for arrival in customers:
            waiting += arrival
            board = min(4, waiting)
            waiting -= board
            rotation += 1
            profit += board * boardingCost - runningCost

            if profit > max_profit:
                max_profit = profit
                best_rotation = rotation

        # Process remaining waiting customers
        # Each rotation boards 4 until the last
        if waiting > 0:
            # Full rotations (4 people each)
            full_rotations = waiting // 4

            # Check if full rotations are profitable
            profit_per_full = 4 * boardingCost - runningCost

            if profit_per_full > 0:
                # Each full rotation is profitable, add them
                for _ in range(full_rotations):
                    waiting -= 4
                    rotation += 1
                    profit += profit_per_full

                    if profit > max_profit:
                        max_profit = profit
                        best_rotation = rotation

                # Handle remaining (< 4)
                if waiting > 0:
                    rotation += 1
                    profit += waiting * boardingCost - runningCost
                    waiting = 0

                    if profit > max_profit:
                        max_profit = profit
                        best_rotation = rotation
            else:
                # Full rotations not profitable, check partial
                # But we still have waiting customers
                while waiting > 0:
                    board = min(4, waiting)
                    waiting -= board
                    rotation += 1
                    profit += board * boardingCost - runningCost

                    if profit > max_profit:
                        max_profit = profit
                        best_rotation = rotation

        return best_rotation


class SolutionSimple:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        """
        Simple simulation without optimization.
        """
        wait = 0
        total_profit = 0
        best_profit = 0
        ans = -1
        turns = 0

        idx = 0
        while idx < len(customers) or wait > 0:
            if idx < len(customers):
                wait += customers[idx]
                idx += 1

            # Board customers
            boarding = min(4, wait)
            wait -= boarding
            turns += 1

            total_profit += boarding * boardingCost - runningCost

            if total_profit > best_profit:
                best_profit = total_profit
                ans = turns

        return ans
