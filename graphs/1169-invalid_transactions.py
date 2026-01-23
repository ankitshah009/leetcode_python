#1169. Invalid Transactions
#Medium
#
#A transaction is possibly invalid if:
#    the amount exceeds $1000, or;
#    if it occurs within (and including) 60 minutes of another transaction
#    with the same name in a different city.
#
#You are given an array of strings transaction where transactions[i] consists
#of comma-separated values representing the name, time, amount, and city of
#the transaction.
#
#Return a list of transactions that are possibly invalid. You may return the
#answer in any order.
#
#Example 1:
#Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
#Output: ["alice,20,800,mtv","alice,50,100,beijing"]
#Explanation: The first transaction is invalid because the second transaction
#occurs within a difference of 60 minutes, have the same name and is in a
#different city.
#
#Example 2:
#Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
#Output: ["alice,50,1200,mtv"]
#
#Example 3:
#Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
#Output: ["bob,50,1200,mtv"]
#
#Constraints:
#    transactions.length <= 1000
#    Each transactions[i] takes the form "{name},{time},{amount},{city}"
#    Each {name} and {city} consist of lowercase English letters, and have
#    lengths between 1 and 10.
#    Each {time} consist of digits, and represent an integer between 0 and 1000.
#    Each {amount} consist of digits, and represent an integer between 0 and 2000.

from typing import List
from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        Parse transactions, check both conditions for each.
        """
        # Parse all transactions
        parsed = []
        for t in transactions:
            parts = t.split(',')
            name, time, amount, city = parts[0], int(parts[1]), int(parts[2]), parts[3]
            parsed.append((name, time, amount, city, t))

        # Group by name
        by_name = defaultdict(list)
        for i, (name, time, amount, city, orig) in enumerate(parsed):
            by_name[name].append((time, city, i))

        invalid = set()

        for i, (name, time, amount, city, orig) in enumerate(parsed):
            # Condition 1: amount > 1000
            if amount > 1000:
                invalid.add(i)

            # Condition 2: same name, different city, within 60 minutes
            for other_time, other_city, j in by_name[name]:
                if i != j and city != other_city and abs(time - other_time) <= 60:
                    invalid.add(i)
                    invalid.add(j)

        return [parsed[i][4] for i in invalid]


class SolutionSimple:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """Simpler O(n^2) approach"""
        n = len(transactions)
        invalid = [False] * n

        # Parse
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))

        for i in range(n):
            name, time, amount, city = parsed[i]

            # Check amount
            if amount > 1000:
                invalid[i] = True

            # Check against all other transactions
            for j in range(n):
                if i == j:
                    continue
                other_name, other_time, _, other_city = parsed[j]
                if name == other_name and city != other_city and abs(time - other_time) <= 60:
                    invalid[i] = True
                    invalid[j] = True

        return [transactions[i] for i in range(n) if invalid[i]]
