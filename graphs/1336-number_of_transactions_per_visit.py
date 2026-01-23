#1336. Number of Transactions per Visit
#Hard
#
#Table: Visits
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| user_id       | int     |
#| visit_date    | date    |
#+---------------+---------+
#(user_id, visit_date) is the primary key for this table.
#
#Table: Transactions
#+------------------+---------+
#| Column Name      | Type    |
#+------------------+---------+
#| user_id          | int     |
#| transaction_date | date    |
#| amount           | int     |
#+------------------+---------+
#There is no primary key for this table.
#
#Write an SQL query to find how many users visited the bank and didn't do any
#transactions, how many visited and did one transaction and so on.
#
#The result table will contain two columns:
#    transactions_count which is the number of transactions done in one visit.
#    visits_count which is the corresponding number of users who did
#    transactions_count in one visit to the bank.
#
#transactions_count should take all values from 0 to max(transactions_count)
#done by one or more users.
#
#Return the result table ordered by transactions_count.

# SQL Solution using recursive CTE:
# WITH RECURSIVE
# visit_transactions AS (
#     SELECT v.user_id, v.visit_date, COUNT(t.user_id) AS transactions_count
#     FROM Visits v
#     LEFT JOIN Transactions t
#         ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
#     GROUP BY v.user_id, v.visit_date
# ),
# max_transactions AS (
#     SELECT IFNULL(MAX(transactions_count), 0) AS max_count FROM visit_transactions
# ),
# numbers AS (
#     SELECT 0 AS n
#     UNION ALL
#     SELECT n + 1 FROM numbers, max_transactions WHERE n < max_count
# )
# SELECT
#     n.n AS transactions_count,
#     COUNT(vt.user_id) AS visits_count
# FROM numbers n
# LEFT JOIN visit_transactions vt ON n.n = vt.transactions_count
# GROUP BY n.n
# ORDER BY n.n;

# Python simulation
from typing import List, Tuple
from datetime import date
from collections import defaultdict, Counter

class Solution:
    def transactionsPerVisit(
        self,
        visits: List[Tuple[int, date]],
        transactions: List[Tuple[int, date, int]]
    ) -> List[Tuple[int, int]]:
        """
        Count transactions per visit, then aggregate.
        Include all counts from 0 to max.
        """
        # Group transactions by (user_id, date)
        trans_by_visit = defaultdict(int)
        for user_id, trans_date, amount in transactions:
            trans_by_visit[(user_id, trans_date)] += 1

        # For each visit, count transactions
        trans_counts = []
        for user_id, visit_date in visits:
            count = trans_by_visit.get((user_id, visit_date), 0)
            trans_counts.append(count)

        # Count visits for each transaction count
        count_freq = Counter(trans_counts)

        # Ensure all values from 0 to max are included
        if not trans_counts:
            return [(0, 0)]

        max_count = max(trans_counts) if trans_counts else 0

        result = []
        for i in range(max_count + 1):
            result.append((i, count_freq.get(i, 0)))

        return result
