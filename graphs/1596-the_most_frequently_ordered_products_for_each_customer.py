#1596. The Most Frequently Ordered Products for Each Customer
#Medium (SQL)
#
#Table: Customers
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| customer_id   | int     |
#| name          | varchar |
#+---------------+---------+
#customer_id is the primary key for this table.
#This table contains information about the customers.
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| order_date    | date    |
#| customer_id   | int     |
#| product_id    | int     |
#+---------------+---------+
#order_id is the primary key for this table.
#This table contains information about the orders made by customer_id.
#
#Table: Products
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| product_name  | varchar |
#| price         | int     |
#+---------------+---------+
#product_id is the primary key for this table.
#This table contains information about the products.
#
#Write an SQL query to find the most frequently ordered product(s) for each customer.
#
#The result table should have the product_id and product_name for each customer_id
#who ordered at least one order. Return the result table in any order.
#
#Example 1:
#Input:
#Customers table:
#+-------------+-------+
#| customer_id | name  |
#+-------------+-------+
#| 1           | Alice |
#| 2           | Bob   |
#| 3           | Tom   |
#| 4           | Jerry |
#| 5           | John  |
#+-------------+-------+
#
#Orders table:
#+----------+------------+-------------+------------+
#| order_id | order_date | customer_id | product_id |
#+----------+------------+-------------+------------+
#| 1        | 2020-07-31 | 1           | 1          |
#| 2        | 2020-07-30 | 2           | 2          |
#| 3        | 2020-08-29 | 3           | 3          |
#| 4        | 2020-07-29 | 4           | 1          |
#| 5        | 2020-06-10 | 1           | 2          |
#| 6        | 2020-08-01 | 2           | 1          |
#| 7        | 2020-08-01 | 3           | 3          |
#| 8        | 2020-08-03 | 1           | 2          |
#| 9        | 2020-08-07 | 2           | 3          |
#| 10       | 2020-07-15 | 1           | 2          |
#+----------+------------+-------------+------------+
#
#Products table:
#+------------+--------------+-------+
#| product_id | product_name | price |
#+------------+--------------+-------+
#| 1          | keyboard     | 120   |
#| 2          | mouse        | 80    |
#| 3          | screen       | 600   |
#| 4          | hard disk    | 450   |
#+------------+--------------+-------+
#
#Output:
#+-------------+------------+--------------+
#| customer_id | product_id | product_name |
#+-------------+------------+--------------+
#| 1           | 2          | mouse        |
#| 2           | 1          | keyboard     |
#| 2           | 2          | mouse        |
#| 2           | 3          | screen       |
#| 3           | 3          | screen       |
#| 4           | 1          | keyboard     |
#+-------------+------------+--------------+

#SQL Solution:
#WITH order_counts AS (
#    SELECT customer_id, product_id, COUNT(*) as cnt
#    FROM Orders
#    GROUP BY customer_id, product_id
#),
#max_counts AS (
#    SELECT customer_id, MAX(cnt) as max_cnt
#    FROM order_counts
#    GROUP BY customer_id
#)
#SELECT oc.customer_id, oc.product_id, p.product_name
#FROM order_counts oc
#JOIN max_counts mc ON oc.customer_id = mc.customer_id AND oc.cnt = mc.max_cnt
#JOIN Products p ON oc.product_id = p.product_id
#ORDER BY oc.customer_id;

from typing import List, Dict
from collections import defaultdict, Counter

class Solution:
    def mostFrequentProducts(
        self,
        orders: List[Dict],
        products: List[Dict]
    ) -> List[Dict]:
        """
        Python simulation: Find most frequent product(s) per customer.
        """
        # Build product name lookup
        product_name = {p['product_id']: p['product_name'] for p in products}

        # Count orders per (customer, product)
        counts = defaultdict(Counter)
        for order in orders:
            cid = order['customer_id']
            pid = order['product_id']
            counts[cid][pid] += 1

        result = []

        for cid, product_counts in counts.items():
            if not product_counts:
                continue

            max_count = max(product_counts.values())

            for pid, cnt in product_counts.items():
                if cnt == max_count:
                    result.append({
                        'customer_id': cid,
                        'product_id': pid,
                        'product_name': product_name[pid]
                    })

        return sorted(result, key=lambda x: x['customer_id'])


class SolutionDetailed:
    def mostFrequentProducts(
        self,
        orders: List[Dict],
        products: List[Dict]
    ) -> List[Dict]:
        """
        Step-by-step solution with intermediate results.
        """
        # Step 1: Count orders per (customer, product)
        order_counts = defaultdict(lambda: defaultdict(int))
        for order in orders:
            order_counts[order['customer_id']][order['product_id']] += 1

        # Step 2: Find max count per customer
        max_counts = {}
        for cid, product_counts in order_counts.items():
            max_counts[cid] = max(product_counts.values())

        # Step 3: Product name lookup
        product_lookup = {p['product_id']: p['product_name'] for p in products}

        # Step 4: Build result
        result = []
        for cid, product_counts in order_counts.items():
            max_cnt = max_counts[cid]
            for pid, cnt in product_counts.items():
                if cnt == max_cnt:
                    result.append({
                        'customer_id': cid,
                        'product_id': pid,
                        'product_name': product_lookup[pid]
                    })

        return result
