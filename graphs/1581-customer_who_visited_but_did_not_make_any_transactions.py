#1581. Customer Who Visited but Did Not Make Any Transactions
#Easy (SQL)
#
#Table: Visits
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| visit_id    | int     |
#| customer_id | int     |
#+-------------+---------+
#visit_id is the primary key for this table.
#This table contains information about the customers who visited the mall.
#
#Table: Transactions
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| transaction_id | int     |
#| visit_id       | int     |
#| amount         | int     |
#+----------------+---------+
#transaction_id is the primary key for this table.
#This table contains information about the transactions made during the visit_id.
#
#Write a SQL query to find the IDs of the users who visited without making any
#transactions and the number of times they made these types of visits.
#
#Return the result table sorted in any order.
#
#Example 1:
#Input:
#Visits
#+----------+-------------+
#| visit_id | customer_id |
#+----------+-------------+
#| 1        | 23          |
#| 2        | 9           |
#| 4        | 30          |
#| 5        | 54          |
#| 6        | 96          |
#| 7        | 54          |
#| 8        | 54          |
#+----------+-------------+
#
#Transactions
#+----------------+----------+--------+
#| transaction_id | visit_id | amount |
#+----------------+----------+--------+
#| 2              | 5        | 310    |
#| 3              | 5        | 300    |
#| 9              | 5        | 200    |
#| 12             | 1        | 910    |
#| 13             | 2        | 970    |
#+----------------+----------+--------+
#
#Output:
#+-------------+----------------+
#| customer_id | count_no_trans |
#+-------------+----------------+
#| 54          | 2              |
#| 30          | 1              |
#| 96          | 1              |
#+-------------+----------------+

#SQL Solution:
#SELECT customer_id, COUNT(*) AS count_no_trans
#FROM Visits v
#LEFT JOIN Transactions t ON v.visit_id = t.visit_id
#WHERE t.visit_id IS NULL
#GROUP BY customer_id;
#
#-- Alternative:
#-- SELECT customer_id, COUNT(*) AS count_no_trans
#-- FROM Visits
#-- WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
#-- GROUP BY customer_id;

from typing import List
from collections import Counter

class Solution:
    def customersWithNoTransactions(
        self,
        visits: List[dict],
        transactions: List[dict]
    ) -> List[dict]:
        """
        Python simulation: Find visits without transactions.
        """
        # Get visit_ids that have transactions
        visits_with_trans = {t['visit_id'] for t in transactions}

        # Find visits without transactions and count by customer
        no_trans_counts = Counter()

        for visit in visits:
            if visit['visit_id'] not in visits_with_trans:
                no_trans_counts[visit['customer_id']] += 1

        return [
            {'customer_id': cid, 'count_no_trans': count}
            for cid, count in no_trans_counts.items()
        ]


class SolutionLeftJoin:
    def customersWithNoTransactions(
        self,
        visits: List[dict],
        transactions: List[dict]
    ) -> List[dict]:
        """
        Simulate left join approach.
        """
        trans_visit_ids = {t['visit_id'] for t in transactions}

        # Left join: keep visits, mark if has transaction
        visits_no_trans = [
            v['customer_id']
            for v in visits
            if v['visit_id'] not in trans_visit_ids
        ]

        # Count
        counts = Counter(visits_no_trans)

        return [
            {'customer_id': cid, 'count_no_trans': cnt}
            for cid, cnt in counts.items()
        ]
