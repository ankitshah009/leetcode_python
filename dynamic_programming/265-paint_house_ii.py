#265. Paint House II
#Hard
#
#There are a row of n houses, each house can be painted with one of the k colors.
#The cost of painting each house with a certain color is different. You have to
#paint all the houses such that no two adjacent houses have the same color.
#
#The cost of painting each house with a certain color is represented by an n x k
#cost matrix costs.
#
#Return the minimum cost to paint all houses.
#
#Example 1:
#Input: costs = [[1,5,3],[2,9,4]]
#Output: 5
#Explanation: Paint house 0 into color 0, paint house 1 into color 2. Total = 1 + 4 = 5
#Or paint house 0 into color 2, paint house 1 into color 0. Total = 3 + 2 = 5.
#
#Example 2:
#Input: costs = [[1,3],[2,4]]
#Output: 5
#
#Constraints:
#    costs.length == n
#    costs[i].length == k
#    1 <= n <= 100
#    2 <= k <= 20
#    1 <= costs[i][j] <= 20
#
#Follow up: Could you solve it in O(nk) runtime?

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])
        if k == 1:
            return costs[0][0] if n == 1 else float('inf')

        # Track minimum and second minimum costs and their indices
        min1, min2 = 0, 0
        idx1 = -1

        for i in range(n):
            new_min1, new_min2 = float('inf'), float('inf')
            new_idx1 = -1

            for j in range(k):
                # Cost = current cost + previous min (excluding same color)
                cost = costs[i][j] + (min1 if j != idx1 else min2)

                if cost < new_min1:
                    new_min2 = new_min1
                    new_min1 = cost
                    new_idx1 = j
                elif cost < new_min2:
                    new_min2 = cost

            min1, min2, idx1 = new_min1, new_min2, new_idx1

        return min1

    # Standard DP approach O(nk^2)
    def minCostIIStandard(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])
        dp = costs[0][:]

        for i in range(1, n):
            new_dp = [0] * k
            for j in range(k):
                # Min cost excluding current color
                new_dp[j] = costs[i][j] + min(dp[l] for l in range(k) if l != j)
            dp = new_dp

        return min(dp)
