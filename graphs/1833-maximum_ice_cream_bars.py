#1833. Maximum Ice Cream Bars
#Medium
#
#It is a sweltering summer day, and a boy wants to buy some ice cream bars.
#
#At the store, there are n ice cream bars. You are given an array costs of
#length n, where costs[i] is the price of the ith ice cream bar in coins. The
#boy initially has coins coins to spend, and he wants to buy as many ice cream
#bars as possible.
#
#Note: The boy can buy the ice cream bars in any order.
#
#Return the maximum number of ice cream bars the boy can buy with coins coins.
#
#You must solve the problem by counting sort.
#
#Example 1:
#Input: costs = [1,3,2,4,1], coins = 5
#Output: 4
#
#Example 2:
#Input: costs = [10,6,8,7,7,8], coins = 5
#Output: 0
#
#Example 3:
#Input: costs = [1,6,3,1,2,5], coins = 20
#Output: 6
#
#Constraints:
#    costs.length == n
#    1 <= n <= 10^5
#    1 <= costs[i] <= 10^5
#    1 <= coins <= 10^8

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Greedy: buy cheapest first.
        """
        costs.sort()
        count = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break

        return count


class SolutionCountingSort:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Using counting sort as required by problem.
        """
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        count = 0
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue

            # How many can we buy at this cost?
            can_buy = min(freq[cost], coins // cost)
            count += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return count


class SolutionHeap:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Using min-heap.
        """
        import heapq

        heapq.heapify(costs)
        count = 0

        while costs and coins >= costs[0]:
            coins -= heapq.heappop(costs)
            count += 1

        return count
