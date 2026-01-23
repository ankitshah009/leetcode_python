#1587. Bank Account Summary II
#Easy (SQL)
#
#Table: Users
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| account       | int     |
#| name          | varchar |
#+---------------+---------+
#account is the primary key for this table.
#Each row of this table contains the account number and the name of the user.
#
#Table: Transactions
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| trans_id      | int     |
#| account       | int     |
#| amount        | int     |
#+---------------+---------+
#trans_id is the primary key for this table.
#Each row of this table contains all changes made to all accounts.
#amount is positive if the user received money and negative if they transferred
#money to another account.
#
#Write an SQL query to report the name and balance of users with a balance
#higher than 10000. The balance of an account is equal to the sum of the
#amounts of all transactions involving that account.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Users table:
#+------------+-----------+
#| account    | name      |
#+------------+-----------+
#| 900001     | Alice     |
#| 900002     | Bob       |
#| 900003     | Charlie   |
#+------------+-----------+
#
#Transactions table:
#+------------+------------+----------+
#| trans_id   | account    | amount   |
#+------------+------------+----------+
#| 1          | 900001     | 7000     |
#| 2          | 900001     | 7000     |
#| 3          | 900001     | -3000    |
#| 4          | 900002     | 1000     |
#| 5          | 900003     | 6000     |
#| 6          | 900003     | 6000     |
#| 7          | 900003     | -4000    |
#+------------+------------+----------+
#
#Output:
#+------------+-----------+
#| name       | balance   |
#+------------+-----------+
#| Alice      | 11000     |
#+------------+-----------+
#Explanation:
#Alice's balance is (7000 + 7000 - 3000) = 11000.
#Bob's balance is 1000.
#Charlie's balance is (6000 + 6000 - 4000) = 8000.

#SQL Solution:
#SELECT u.name, SUM(t.amount) AS balance
#FROM Users u
#JOIN Transactions t ON u.account = t.account
#GROUP BY u.account, u.name
#HAVING SUM(t.amount) > 10000;

from typing import List, Dict
from collections import defaultdict

class Solution:
    def bankAccountSummary(
        self,
        users: List[Dict],
        transactions: List[Dict]
    ) -> List[Dict]:
        """
        Python simulation: Find users with balance > 10000.
        """
        # Calculate balance per account
        balance = defaultdict(int)
        for t in transactions:
            balance[t['account']] += t['amount']

        # Build account to name mapping
        account_name = {u['account']: u['name'] for u in users}

        # Filter and return
        result = []
        for account, total in balance.items():
            if total > 10000:
                result.append({
                    'name': account_name[account],
                    'balance': total
                })

        return result


class SolutionJoin:
    def bankAccountSummary(
        self,
        users: List[Dict],
        transactions: List[Dict]
    ) -> List[Dict]:
        """
        Simulate SQL join approach.
        """
        # Create name lookup
        name_map = {u['account']: u['name'] for u in users}

        # Sum transactions by account
        totals = defaultdict(int)
        for t in transactions:
            totals[t['account']] += t['amount']

        # Filter by balance > 10000
        return [
            {'name': name_map[acc], 'balance': bal}
            for acc, bal in totals.items()
            if bal > 10000
        ]
