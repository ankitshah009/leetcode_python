#1475. Final Prices With a Special Discount in a Shop
#Easy
#
#You are given an integer array prices where prices[i] is the price of the ith
#item in a shop.
#
#There is a special discount for items in the shop. If you buy the ith item,
#then you will receive a discount equivalent to prices[j] where j is the minimum
#index such that j > i and prices[j] <= prices[i]. Otherwise, you will not
#receive any discount at all.
#
#Return an integer array answer where answer[i] is the final price you will pay
#for the ith item of the shop, considering the special discount.
#
#Example 1:
#Input: prices = [8,4,6,2,3]
#Output: [4,2,4,2,3]
#Explanation:
#For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4,
#therefore, the final price you will pay is 8 - 4 = 4.
#For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2,
#therefore, the final price you will pay is 4 - 2 = 2.
#For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2,
#therefore, the final price you will pay is 6 - 2 = 4.
#For items 3 and 4 you will not receive any discount at all.
#
#Example 2:
#Input: prices = [1,2,3,4,5]
#Output: [1,2,3,4,5]
#Explanation: In this case, for all items, you will not receive any discount at all.
#
#Example 3:
#Input: prices = [10,1,1,6]
#Output: [9,0,1,6]
#
#Constraints:
#    1 <= prices.length <= 500
#    1 <= prices[i] <= 1000

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Monotonic stack: find next smaller or equal element.
        """
        n = len(prices)
        result = prices.copy()
        stack = []  # Stack of indices

        for i in range(n):
            # Pop elements that found their discount
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]

            stack.append(i)

        return result


class SolutionBruteForce:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """Brute force O(n^2) solution"""
        n = len(prices)
        result = prices.copy()

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break

        return result


class SolutionRightToLeft:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Process right to left with monotonic stack.
        Stack maintains potential discounts for items on the left.
        """
        n = len(prices)
        result = prices.copy()
        stack = []  # Stack of prices (monotonically increasing)

        for i in range(n - 1, -1, -1):
            # Remove prices that are too large to be a discount
            while stack and stack[-1] > prices[i]:
                stack.pop()

            # Apply discount if available
            if stack:
                result[i] = prices[i] - stack[-1]

            stack.append(prices[i])

        return result


class SolutionOnePass:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """One-pass solution with stack storing (index, price)"""
        result = prices.copy()
        stack = []  # (index, price)

        for i, price in enumerate(prices):
            while stack and price <= stack[-1][1]:
                idx, p = stack.pop()
                result[idx] = p - price
            stack.append((i, price))

        return result
