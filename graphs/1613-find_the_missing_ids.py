#1613. Find the Missing IDs
#Medium (SQL)
#
#Table: Customers
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| customer_id   | int     |
#| customer_name | varchar |
#+---------------+---------+
#customer_id is the primary key for this table.
#Each row of this table contains the name and the id of a customer.
#
#Write an SQL query to find the missing customer IDs. The missing IDs are ones
#that are not in the Customers table but are in the range between 1 and the
#maximum customer_id present in the table.
#
#Notice that the maximum customer_id will not exceed 100.
#
#Return the result table ordered by ids in ascending order.
#
#Example 1:
#Input:
#Customers table:
#+-------------+---------------+
#| customer_id | customer_name |
#+-------------+---------------+
#| 1           | Alice         |
#| 4           | Bob           |
#| 5           | Charlie       |
#+-------------+---------------+
#
#Output:
#+-----+
#| ids |
#+-----+
#| 2   |
#| 3   |
#+-----+
#Explanation:
#The maximum customer_id present in the table is 5, so in the range [1,5],
#IDs 2 and 3 are missing from the table.

#SQL Solution (using recursive CTE):
#WITH RECURSIVE seq AS (
#    SELECT 1 AS n
#    UNION ALL
#    SELECT n + 1 FROM seq WHERE n < (SELECT MAX(customer_id) FROM Customers)
#)
#SELECT n AS ids
#FROM seq
#WHERE n NOT IN (SELECT customer_id FROM Customers)
#ORDER BY ids;
#
#-- Alternative with numbers table:
#-- SELECT n AS ids FROM Numbers
#-- WHERE n <= (SELECT MAX(customer_id) FROM Customers)
#-- AND n NOT IN (SELECT customer_id FROM Customers);

from typing import List, Dict

class Solution:
    def findMissingIds(self, customers: List[Dict]) -> List[int]:
        """
        Python simulation: Find missing IDs in range [1, max_id].
        """
        if not customers:
            return []

        existing_ids = {c['customer_id'] for c in customers}
        max_id = max(existing_ids)

        missing = []
        for i in range(1, max_id + 1):
            if i not in existing_ids:
                missing.append(i)

        return missing


class SolutionSet:
    def findMissingIds(self, customers: List[Dict]) -> List[int]:
        """
        Using set difference.
        """
        if not customers:
            return []

        existing = {c['customer_id'] for c in customers}
        max_id = max(existing)

        all_ids = set(range(1, max_id + 1))
        missing = sorted(all_ids - existing)

        return missing


class SolutionComprehension:
    def findMissingIds(self, customers: List[Dict]) -> List[int]:
        """
        List comprehension approach.
        """
        if not customers:
            return []

        ids = {c['customer_id'] for c in customers}
        max_id = max(ids)

        return [i for i in range(1, max_id + 1) if i not in ids]
