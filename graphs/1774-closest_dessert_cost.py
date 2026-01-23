#1774. Closest Dessert Cost
#Medium
#
#You would like to make dessert and are preparing to buy the ingredients. You
#have n ice cream base flavors and m types of toppings to choose from. You must
#follow these rules when making your dessert:
#
#- There must be exactly one ice cream base.
#- You can add one or more types of topping or have no topping at all.
#- There are at most two of each type of topping.
#
#You are given three inputs:
#- baseCosts, an integer array of length n, where each baseCosts[i] represents
#  the price of the ith ice cream base flavor.
#- toppingCosts, an integer array of length m, where each toppingCosts[i] is the
#  price of one of the ith topping.
#- target, an integer representing your target price for dessert.
#
#You want to make a dessert with a total cost as close to target as possible.
#
#Return the closest possible cost of the dessert to target. If there are multiple,
#return the lower one.
#
#Example 1:
#Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
#Output: 10
#
#Example 2:
#Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
#Output: 17
#
#Example 3:
#Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
#Output: 8
#
#Constraints:
#    n == baseCosts.length
#    m == toppingCosts.length
#    1 <= n, m <= 10
#    1 <= baseCosts[i], toppingCosts[i] <= 10^4
#    1 <= target <= 10^4

from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        Generate all possible topping combinations, then try each base.
        """
        # Generate all topping sums (0, 1, or 2 of each)
        topping_sums = {0}
        for cost in toppingCosts:
            new_sums = set()
            for s in topping_sums:
                new_sums.add(s)
                new_sums.add(s + cost)
                new_sums.add(s + 2 * cost)
            topping_sums = new_sums

        closest = float('inf')

        for base in baseCosts:
            for topping in topping_sums:
                cost = base + topping
                # Update if closer, or same distance but lower
                if (abs(cost - target) < abs(closest - target) or
                    (abs(cost - target) == abs(closest - target) and cost < closest)):
                    closest = cost

        return closest


class SolutionDFS:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        DFS to explore topping combinations.
        """
        self.closest = min(baseCosts)  # Start with cheapest base only

        def dfs(idx: int, current: int):
            # Update closest
            if (abs(current - target) < abs(self.closest - target) or
                (abs(current - target) == abs(self.closest - target) and current < self.closest)):
                self.closest = current

            # Pruning: if already over target, adding more won't help
            if idx == len(toppingCosts) or current > target:
                return

            # Try 0, 1, 2 of current topping
            dfs(idx + 1, current)
            dfs(idx + 1, current + toppingCosts[idx])
            dfs(idx + 1, current + 2 * toppingCosts[idx])

        for base in baseCosts:
            dfs(0, base)

        return self.closest


class SolutionBitMask:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        Bitmask enumeration for toppings (ternary).
        """
        m = len(toppingCosts)
        closest = baseCosts[0]

        # Each topping can be 0, 1, or 2 -> 3^m combinations
        for base in baseCosts:
            for mask in range(3 ** m):
                cost = base
                temp = mask
                for j in range(m):
                    cost += (temp % 3) * toppingCosts[j]
                    temp //= 3

                if (abs(cost - target) < abs(closest - target) or
                    (abs(cost - target) == abs(closest - target) and cost < closest)):
                    closest = cost

        return closest
