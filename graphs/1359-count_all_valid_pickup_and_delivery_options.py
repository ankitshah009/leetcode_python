#1359. Count All Valid Pickup and Delivery Options
#Hard
#
#Given n orders, each order consist in pickup and delivery services.
#
#Count all valid pickup/delivery possible sequences such that delivery(i) is
#always after of pickup(i).
#
#Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 1
#Output: 1
#Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
#
#Example 2:
#Input: n = 2
#Output: 6
#Explanation: All possible orders:
#(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
#This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
#
#Example 3:
#Input: n = 3
#Output: 90
#
#Constraints:
#    1 <= n <= 500

class Solution:
    def countOrders(self, n: int) -> int:
        """
        For n orders, we have 2n positions.

        Build incrementally:
        - For 1 order: 1 way (P1, D1)
        - For 2 orders: place P2 and D2 in 2*1 + 1 = 3 positions for P2,
          then D2 must come after P2 (gives (3 * 2) / 2 = 3 ways per existing arrangement)

        For n orders: multiply previous result by (2n-1 + 2n-2 + ... + 1) = (2n-1) * n
        Or equivalently: (2n-1) * (2n) / 2 = (2n-1) * n
        """
        MOD = 10**9 + 7

        result = 1
        for i in range(2, n + 1):
            # Number of ways to insert the i-th pickup-delivery pair
            # into existing sequence of 2*(i-1) items
            # We have 2i-1 choices for pickup, then (2i-1 + 2i-2 + ... + 1) / 2 = (2i-1)*i
            # choices that place delivery after pickup
            slots = 2 * i - 1
            ways = slots * i
            result = (result * ways) % MOD

        return result


class SolutionDP:
    def countOrders(self, n: int) -> int:
        """DP approach"""
        MOD = 10**9 + 7

        # dp[i] = number of valid sequences for i orders
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # Insert P_i and D_i into sequence of 2*(i-1) items
            # P_i can go in any of 2*(i-1) + 1 = 2i-1 positions
            # D_i must go after P_i: if P_i is at position k, D_i has (2i-1-k) choices
            # Total: sum from k=0 to 2i-2 of (2i-1-k) = (2i-1) + (2i-2) + ... + 1 = (2i-1)*i
            dp[i] = dp[i-1] * (2*i - 1) * i % MOD

        return dp[n]


class SolutionMath:
    def countOrders(self, n: int) -> int:
        """
        Mathematical approach:
        Total arrangements = (2n)! / 2^n

        - (2n)! arranges all 2n items
        - Divide by 2^n because for each order, P must come before D
        """
        MOD = 10**9 + 7

        # Compute (2n)! / 2^n mod MOD
        # = (2n)! * inverse(2^n) mod MOD
        # = (2n * (2n-1) * ... * 1) / (2 * 2 * ... * 2)
        # = n! * (2n-1) * (2n-3) * ... * 1

        result = 1
        for i in range(1, n + 1):
            result = result * i % MOD  # n!
            result = result * (2 * i - 1) % MOD  # multiply by odd numbers

        return result
