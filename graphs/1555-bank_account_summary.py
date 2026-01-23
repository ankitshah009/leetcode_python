#1555. Bank Account Summary
#Medium (SQL)
#
#Table: Users
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| user_id       | int     |
#| user_name     | varchar |
#| credit        | int     |
#+---------------+---------+
#user_id is the primary key for this table.
#Each row of this table contains the current credit information for each user.
#
#Table: Transactions
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| trans_id      | int     |
#| paid_by       | int     |
#| paid_to       | int     |
#| amount        | int     |
#| transacted_on | date    |
#+---------------+---------+
#trans_id is the primary key for this table.
#Each row of this table contains information about the transaction in the bank.
#User with id (paid_by) transfer (amount) to user with id (paid_to).
#
#Write an SQL query to report:
#- user_id,
#- user_name,
#- credit, current balance after performing all transactions, and
#- credit_limit_breached, check credit_limit ("Yes" or "No")
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Users table:
#+---------+-----------+--------+
#| user_id | user_name | credit |
#+---------+-----------+--------+
#| 1       | Moustafa  | 100    |
#| 2       | Jonathan  | 200    |
#| 3       | Winston   | 10000  |
#| 4       | Luis      | 800    |
#+---------+-----------+--------+
#
#Transactions table:
#+----------+----------+----------+--------+---------------+
#| trans_id | paid_by  | paid_to  | amount | transacted_on |
#+----------+----------+----------+--------+---------------+
#| 1        | 1        | 3        | 400    | 2020-08-01    |
#| 2        | 3        | 2        | 500    | 2020-08-02    |
#| 3        | 2        | 1        | 200    | 2020-08-03    |
#+----------+----------+----------+--------+---------------+
#
#Output:
#+---------+-----------+--------+-----------------------+
#| user_id | user_name | credit | credit_limit_breached |
#+---------+-----------+--------+-----------------------+
#| 1       | Moustafa  | -100   | Yes                   |
#| 2       | Jonathan  | 500    | No                    |
#| 3       | Winston   | 9900   | No                    |
#| 4       | Luis      | 800    | No                    |
#+---------+-----------+--------+-----------------------+

#SQL Solution:
#SELECT
#    u.user_id,
#    u.user_name,
#    u.credit + IFNULL(received.total, 0) - IFNULL(sent.total, 0) AS credit,
#    CASE
#        WHEN u.credit + IFNULL(received.total, 0) - IFNULL(sent.total, 0) < 0 THEN 'Yes'
#        ELSE 'No'
#    END AS credit_limit_breached
#FROM Users u
#LEFT JOIN (
#    SELECT paid_to AS user_id, SUM(amount) AS total
#    FROM Transactions
#    GROUP BY paid_to
#) received ON u.user_id = received.user_id
#LEFT JOIN (
#    SELECT paid_by AS user_id, SUM(amount) AS total
#    FROM Transactions
#    GROUP BY paid_by
#) sent ON u.user_id = sent.user_id;

from typing import List
from collections import defaultdict

class Solution:
    def bankAccountSummary(
        self,
        users: List[dict],
        transactions: List[dict]
    ) -> List[dict]:
        """
        Python simulation: Calculate final credit after all transactions.
        """
        # Calculate net change for each user
        net_change = defaultdict(int)

        for trans in transactions:
            paid_by = trans['paid_by']
            paid_to = trans['paid_to']
            amount = trans['amount']

            net_change[paid_by] -= amount
            net_change[paid_to] += amount

        # Build result
        result = []
        for user in users:
            uid = user['user_id']
            final_credit = user['credit'] + net_change[uid]

            result.append({
                'user_id': uid,
                'user_name': user['user_name'],
                'credit': final_credit,
                'credit_limit_breached': 'Yes' if final_credit < 0 else 'No'
            })

        return result


class SolutionDetailed:
    def bankAccountSummary(
        self,
        users: List[dict],
        transactions: List[dict]
    ) -> List[dict]:
        """
        Calculate sent and received separately for clarity.
        """
        # Sum amounts sent by each user
        sent = defaultdict(int)
        for trans in transactions:
            sent[trans['paid_by']] += trans['amount']

        # Sum amounts received by each user
        received = defaultdict(int)
        for trans in transactions:
            received[trans['paid_to']] += trans['amount']

        # Build result
        result = []
        for user in users:
            uid = user['user_id']
            initial = user['credit']
            final_credit = initial + received[uid] - sent[uid]

            result.append({
                'user_id': uid,
                'user_name': user['user_name'],
                'credit': final_credit,
                'credit_limit_breached': 'Yes' if final_credit < 0 else 'No'
            })

        return result


class SolutionSimulation:
    def bankAccountSummary(
        self,
        users: List[dict],
        transactions: List[dict]
    ) -> List[dict]:
        """
        Simulate transactions step by step.
        """
        # Create a copy of user credits
        credits = {u['user_id']: u['credit'] for u in users}

        # Process each transaction
        for trans in transactions:
            credits[trans['paid_by']] -= trans['amount']
            credits[trans['paid_to']] += trans['amount']

        # Build result
        return [
            {
                'user_id': u['user_id'],
                'user_name': u['user_name'],
                'credit': credits[u['user_id']],
                'credit_limit_breached': 'Yes' if credits[u['user_id']] < 0 else 'No'
            }
            for u in users
        ]
