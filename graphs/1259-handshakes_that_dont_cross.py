#1259. Handshakes That Don't Cross
#Hard
#
#You are given an even number of people numPeople that stand around a circle
#and each person shakes hands with someone else so that there are numPeople / 2
#handshakes total.
#
#Return the number of ways these handshakes could occur such that none of the
#handshakes cross.
#
#Since the answer could be very large, return it mod 10^9 + 7.
#
#Example 1:
#Input: numPeople = 4
#Output: 2
#Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and
#the second one is [(2,3),(4,1)].
#
#Example 2:
#Input: numPeople = 6
#Output: 5
#
#Example 3:
#Input: numPeople = 8
#Output: 14
#
#Constraints:
#    2 <= numPeople <= 1000
#    numPeople is even.

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        """
        This is the Catalan number sequence!
        C(n) = C(0)*C(n-1) + C(1)*C(n-2) + ... + C(n-1)*C(0)

        When person 1 shakes with person k (k must be even for non-crossing):
        - People 2 to k-1 form one group
        - People k+1 to n form another group
        Both groups must independently solve the same problem.
        """
        MOD = 10**9 + 7
        n = numPeople // 2  # Number of pairs

        # dp[i] = number of ways for 2*i people
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 0 people = 1 way

        for i in range(1, n + 1):
            # Person 1 shakes with person 2*k (k from 1 to i)
            for k in range(1, i + 1):
                # k-1 pairs between them, i-k pairs after
                dp[i] = (dp[i] + dp[k - 1] * dp[i - k]) % MOD

        return dp[n]


class SolutionCatalan:
    def numberOfWays(self, numPeople: int) -> int:
        """
        Direct Catalan number formula:
        C(n) = binomial(2n, n) / (n + 1)

        Using modular inverse for division.
        """
        MOD = 10**9 + 7
        n = numPeople // 2

        def mod_pow(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = result * base % mod
                base = base * base % mod
                exp //= 2
            return result

        def mod_inverse(a, mod):
            return mod_pow(a, mod - 2, mod)

        # Calculate binomial(2n, n)
        numerator = 1
        for i in range(2 * n, n, -1):
            numerator = numerator * i % MOD

        denominator = 1
        for i in range(1, n + 1):
            denominator = denominator * i % MOD

        binomial = numerator * mod_inverse(denominator, MOD) % MOD

        # Divide by (n + 1)
        return binomial * mod_inverse(n + 1, MOD) % MOD
