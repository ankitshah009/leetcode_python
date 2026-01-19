#322. Coin Change
#Medium
#
#You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#Example 1:
#
#Input: coins = [1, 2, 5], amount = 11
#Output: 3 
#Explanation: 11 = 5 + 5 + 1
#
#Example 2:
#
#Input: coins = [2], amount = 3
#Output: -1
#
#Note:
#You may assume that you have an infinite number of each kind of coin.
#

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Establish keeping track of min change for each sub-amount
        minCoins = [float("inf")] * (amount + 1)
        minCoins[0] = 0
        for coin in coins:
            for subamount in range(0, len(minCoins)):
                if subamount >= coin:
                    # Take min of either current value or ways of (subamount - coin) + 1
                    minCoins[subamount] = min(minCoins[subamount], minCoins[subamount - coin] + 1)
        return minCoins[-1] if minCoins[-1] != float("inf") else -1



public class Solution {

    public int coinChange(int[] coins, int amount) {        
        if (amount < 1) return 0;
        return coinChange(coins, amount, new int[amount]);
    }

    private int coinChange(int[] coins, int rem, int[] count) {
        if (rem < 0) return -1;
        if (rem == 0) return 0;
        if (count[rem - 1] != 0) return count[rem - 1];
        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int res = coinChange(coins, rem - coin, count);
            if (res >= 0 && res < min)
                min = 1 + res;
        }
        count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
        return count[rem - 1];
    }
}




public class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;             
        int[] dp = new int[amount + 1];  
        Arrays.fill(dp, max);  
        dp[0] = 0;   
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
