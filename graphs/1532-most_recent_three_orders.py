#1532. The Most Recent Three Orders
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
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| order_date    | date    |
#| customer_id   | int     |
#| cost          | int     |
#+---------------+---------+
#order_id is the primary key for this table.
#customer_id is a foreign key of the customer_id from the Customers table.
#
#Write an SQL query to find the most recent three orders of each user. If a user
#ordered less than three orders, return all of their orders.
#
#Return the result table ordered by customer_name in ascending order and in case
#of a tie by the customer_id in ascending order. If there is still a tie, order
#them by order_date in descending order.
#
#Example 1:
#Input:
#Customers table:
#+-------------+-----------+
#| customer_id | name      |
#+-------------+-----------+
#| 1           | Winston   |
#| 2           | Jonathan  |
#| 3           | Annabelle |
#| 4           | Marber    |
#| 5           | David     |
#+-------------+-----------+
#
#Orders table:
#+----------+------------+-------------+------+
#| order_id | order_date | customer_id | cost |
#+----------+------------+-------------+------+
#| 1        | 2020-07-31 | 1           | 30   |
#| 2        | 2020-07-30 | 2           | 40   |
#| 3        | 2020-07-31 | 3           | 70   |
#| 4        | 2020-07-29 | 4           | 100  |
#| 5        | 2020-06-10 | 1           | 1010 |
#| 6        | 2020-08-01 | 2           | 102  |
#| 7        | 2020-08-01 | 3           | 111  |
#| 8        | 2020-08-03 | 1           | 99   |
#| 9        | 2020-08-07 | 2           | 890  |
#| 10       | 2020-07-15 | 1           | 2    |
#+----------+------------+-------------+------+
#
#Output:
#+---------------+-------------+----------+------------+
#| customer_name | customer_id | order_id | order_date |
#+---------------+-------------+----------+------------+
#| Annabelle     | 3           | 7        | 2020-08-01 |
#| Annabelle     | 3           | 3        | 2020-07-31 |
#| David         | 5           | null     | null       |
#| Jonathan      | 2           | 9        | 2020-08-07 |
#| Jonathan      | 2           | 6        | 2020-08-01 |
#| Jonathan      | 2           | 2        | 2020-07-30 |
#| Marber        | 4           | 4        | 2020-07-29 |
#| Winston       | 1           | 8        | 2020-08-03 |
#| Winston       | 1           | 1        | 2020-07-31 |
#| Winston       | 1           | 10       | 2020-07-15 |
#+---------------+-------------+----------+------------+

#SQL Solution:
#SELECT c.name AS customer_name, c.customer_id, o.order_id, o.order_date
#FROM Customers c
#LEFT JOIN Orders o ON c.customer_id = o.customer_id
#WHERE o.order_id IS NULL OR (
#    SELECT COUNT(*)
#    FROM Orders o2
#    WHERE o2.customer_id = o.customer_id AND o2.order_date > o.order_date
#) < 3
#ORDER BY c.name, c.customer_id, o.order_date DESC;
#
#-- Alternative with ROW_NUMBER():
#-- WITH RankedOrders AS (
#--     SELECT o.*, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) as rn
#--     FROM Orders o
#-- )
#-- SELECT c.name AS customer_name, c.customer_id, r.order_id, r.order_date
#-- FROM Customers c
#-- LEFT JOIN RankedOrders r ON c.customer_id = r.customer_id AND r.rn <= 3
#-- ORDER BY c.name, c.customer_id, r.order_date DESC;

from typing import List, Optional
from collections import defaultdict
import heapq

class Solution:
    def mostRecentThreeOrders(
        self,
        customers: List[dict],
        orders: List[dict]
    ) -> List[dict]:
        """
        Python simulation: Get top 3 most recent orders per customer.
        """
        # Group orders by customer
        customer_orders = defaultdict(list)
        for order in orders:
            customer_orders[order['customer_id']].append(order)

        result = []

        # Sort customers by name, then customer_id
        sorted_customers = sorted(customers, key=lambda x: (x['name'], x['customer_id']))

        for customer in sorted_customers:
            cid = customer['customer_id']
            cname = customer['name']

            if cid not in customer_orders:
                # No orders
                result.append({
                    'customer_name': cname,
                    'customer_id': cid,
                    'order_id': None,
                    'order_date': None
                })
            else:
                # Get top 3 by order_date descending
                cust_orders = sorted(
                    customer_orders[cid],
                    key=lambda x: x['order_date'],
                    reverse=True
                )[:3]

                for order in cust_orders:
                    result.append({
                        'customer_name': cname,
                        'customer_id': cid,
                        'order_id': order['order_id'],
                        'order_date': order['order_date']
                    })

        return result


class SolutionHeap:
    def mostRecentThreeOrders(
        self,
        customers: List[dict],
        orders: List[dict]
    ) -> List[dict]:
        """
        Using heap to get top 3 orders efficiently.
        """
        # Build map of customer_id to name
        id_to_name = {c['customer_id']: c['name'] for c in customers}

        # For each customer, maintain min-heap of size 3
        customer_top3 = defaultdict(list)

        for order in orders:
            cid = order['customer_id']
            heap = customer_top3[cid]

            # Use negative date for max-heap behavior with min-heap
            entry = (order['order_date'], order['order_id'])

            if len(heap) < 3:
                heapq.heappush(heap, entry)
            elif entry > heap[0]:
                heapq.heapreplace(heap, entry)

        # Build result
        result = []
        sorted_customers = sorted(customers, key=lambda x: (x['name'], x['customer_id']))

        for customer in sorted_customers:
            cid = customer['customer_id']
            cname = customer['name']

            if cid not in customer_top3:
                result.append({
                    'customer_name': cname,
                    'customer_id': cid,
                    'order_id': None,
                    'order_date': None
                })
            else:
                # Sort by date descending
                top_orders = sorted(customer_top3[cid], reverse=True)
                for date, oid in top_orders:
                    result.append({
                        'customer_name': cname,
                        'customer_id': cid,
                        'order_id': oid,
                        'order_date': date
                    })

        return result
