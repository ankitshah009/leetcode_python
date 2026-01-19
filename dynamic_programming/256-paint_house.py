#256. Paint House
#Medium
#
#There is a row of n houses, where each house can be painted one of three colors:
#red, blue, or green. The cost of painting each house with a certain color is
#different. You have to paint all the houses such that no two adjacent houses
#have the same color.
#
#The cost of painting each house with a certain color is represented by an n x 3
#cost matrix costs.
#
#Return the minimum cost to paint all houses.
#
#Example 1:
#Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
#Output: 10
#Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
#into blue. Minimum cost: 2 + 5 + 3 = 10.
#
#Example 2:
#Input: costs = [[7,6,2]]
#Output: 2
#
#Constraints:
#    costs.length == n
#    costs[i].length == 3
#    1 <= n <= 100
#    1 <= costs[i][j] <= 20

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)

        # dp[i][j] = min cost to paint houses 0..i with house i painted color j
        # j: 0=red, 1=blue, 2=green
        dp = [[0] * 3 for _ in range(n)]

        # Base case: first house
        dp[0] = costs[0][:]

        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

        return min(dp[n-1])

    # Space-optimized version
    def minCostOptimized(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        prev = costs[0][:]

        for i in range(1, len(costs)):
            curr = [
                costs[i][0] + min(prev[1], prev[2]),
                costs[i][1] + min(prev[0], prev[2]),
                costs[i][2] + min(prev[0], prev[1])
            ]
            prev = curr

        return min(prev)
