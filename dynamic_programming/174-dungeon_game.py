#174. Dungeon Game
#Hard
#
#The demons had captured the princess and imprisoned her in the bottom-right corner
#of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid.
#
#Our valiant knight was initially positioned in the top-left room and must fight
#his way through dungeon to rescue the princess.
#
#The knight has an initial health point represented by a positive integer. If at
#any point his health point drops to 0 or below, he dies immediately.
#
#Some rooms are guarded by demons (negative integers), other rooms either contain
#magic orbs that increase health (positive integers) or are empty (0).
#
#To reach the princess as quickly as possible, the knight decides to move only
#rightward or downward in each step.
#
#Return the knight's minimum initial health so that he can rescue the princess.
#
#Example 1:
#Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
#Output: 7
#Explanation: The initial health of the knight must be at least 7 if he follows
#the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
#
#Example 2:
#Input: dungeon = [[0]]
#Output: 1
#
#Constraints:
#    m == dungeon.length
#    n == dungeon[i].length
#    1 <= m, n <= 200
#    -1000 <= dungeon[i][j] <= 1000

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # dp[i][j] = minimum health needed to reach princess from (i,j)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # Base case: need at least 1 health after reaching princess
        dp[m][n-1] = dp[m-1][n] = 1

        # Fill from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health_needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                # Health must be at least 1
                dp[i][j] = max(1, min_health_needed)

        return dp[0][0]

    # Space-optimized version
    def calculateMinimumHPOptimized(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * (n + 1)
        dp[n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j+1]) - dungeon[i][j])
            dp[n] = float('inf')  # Reset boundary for next row

        return dp[0]
