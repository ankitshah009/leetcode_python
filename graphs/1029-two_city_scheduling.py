#1029. Two City Scheduling
#Medium
#
#A company is planning to interview 2n people. Given the array costs where
#costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a
#is aCosti, and the cost of flying the ith person to city b is bCosti.
#
#Return the minimum cost to fly every person to a city such that exactly n
#people arrive in each city.
#
#Example 1:
#Input: costs = [[10,20],[30,11],[400,50],[30,20]]
#Output: 110
#Explanation:
#The first person goes to city a for a cost of 10.
#The second person goes to city b for a cost of 11.
#The third person goes to city b for a cost of 50.
#The fourth person goes to city a for a cost of 30.
#The total minimum cost is 10 + 11 + 50 + 30 = 110.
#
#Example 2:
#Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
#Output: 1859
#
#Example 3:
#Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],
#               [650,359],[631,42]]
#Output: 3086
#
#Constraints:
#    2 * n == costs.length
#    2 <= costs.length <= 100
#    costs.length is even.
#    1 <= aCosti, bCosti <= 1000

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Greedy: Sort by difference (cost_a - cost_b).
        First n people go to city A, rest to city B.

        Intuition: People with larger (cost_a - cost_b) should go to B.
        """
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        total = 0

        for i in range(n):
            total += costs[i][0]  # First n to city A
        for i in range(n, 2 * n):
            total += costs[i][1]  # Rest to city B

        return total


class SolutionDP:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        DP: dp[i][j] = min cost to assign first i people with j going to city A
        """
        n = len(costs) // 2
        INF = float('inf')

        # dp[j] = min cost with j people assigned to city A
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i, (a, b) in enumerate(costs):
            # Process in reverse to avoid using updated values
            new_dp = [INF] * (n + 1)
            for j in range(min(i + 1, n) + 1):
                # Send to city B
                if j <= n and i - j < n:
                    new_dp[j] = min(new_dp[j], dp[j] + b)
                # Send to city A
                if j > 0:
                    new_dp[j] = min(new_dp[j], dp[j-1] + a)
            dp = new_dp

        return dp[n]


class SolutionRefund:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Alternative view: Initially send everyone to A,
        then 'refund' n people by sending them to B instead.
        Refund = cost_b - cost_a (negative if B is cheaper)
        """
        total = sum(a for a, b in costs)

        # Compute refunds and sort
        refunds = [b - a for a, b in costs]
        refunds.sort()

        # Take n cheapest refunds
        n = len(costs) // 2
        total += sum(refunds[:n])

        return total
