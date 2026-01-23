#1672. Richest Customer Wealth
#Easy
#
#You are given an m x n integer grid accounts where accounts[i][j] is the
#amount of money the ith customer has in the jth bank. Return the wealth that
#the richest customer has.
#
#A customer's wealth is the amount of money they have in all their bank accounts.
#The richest customer is the customer that has the maximum wealth.
#
#Example 1:
#Input: accounts = [[1,2,3],[3,2,1]]
#Output: 6
#Explanation: Customer 0 has wealth 6, Customer 1 has wealth 6. Both are richest.
#
#Example 2:
#Input: accounts = [[1,5],[7,3],[3,5]]
#Output: 10
#Explanation: Customer 0 = 6, Customer 1 = 10, Customer 2 = 8. Customer 1 is richest.
#
#Example 3:
#Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
#Output: 17
#
#Constraints:
#    m == accounts.length
#    n == accounts[i].length
#    1 <= m, n <= 50
#    1 <= accounts[i][j] <= 100

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Find max sum of each row.
        """
        return max(sum(customer) for customer in accounts)


class SolutionExplicit:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Explicit loop implementation.
        """
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)

        return max_wealth


class SolutionMap:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Using map function.
        """
        return max(map(sum, accounts))


class SolutionReduce:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Using reduce.
        """
        from functools import reduce
        return reduce(lambda mx, acc: max(mx, sum(acc)), accounts, 0)


class SolutionNumpy:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        NumPy approach (for illustration).
        """
        # import numpy as np
        # return int(np.array(accounts).sum(axis=1).max())
        return max(sum(row) for row in accounts)
