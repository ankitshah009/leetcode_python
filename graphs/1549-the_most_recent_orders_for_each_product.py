#1549. The Most Recent Orders for Each Product
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
#| product_id    | int     |
#+---------------+---------+
#order_id is the primary key for this table.
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
#
#Write an SQL query to find the most recent order(s) of each product.
#
#Return the result table ordered by product_name in ascending order and in case
#of a tie by the product_id in ascending order. If there is still a tie, order
#them by order_id in ascending order.
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
#+----------+------------+-------------+------------+
#| order_id | order_date | customer_id | product_id |
#+----------+------------+-------------+------------+
#| 1        | 2020-07-31 | 1           | 1          |
#| 2        | 2020-07-30 | 2           | 2          |
#| 3        | 2020-08-29 | 3           | 3          |
#| 4        | 2020-07-29 | 4           | 1          |
#| 5        | 2020-06-10 | 1           | 2          |
#| 6        | 2020-08-01 | 2           | 1          |
#| 7        | 2020-08-01 | 3           | 1          |
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
#+--------------+------------+----------+------------+
#| product_name | product_id | order_id | order_date |
#+--------------+------------+----------+------------+
#| keyboard     | 1          | 6        | 2020-08-01 |
#| keyboard     | 1          | 7        | 2020-08-01 |
#| mouse        | 2          | 8        | 2020-08-03 |
#| screen       | 3          | 3        | 2020-08-29 |
#| screen       | 3          | 9        | 2020-08-07 |
#+------------+--------------+----------+------------+

#SQL Solution:
#SELECT p.product_name, p.product_id, o.order_id, o.order_date
#FROM Products p
#JOIN Orders o ON p.product_id = o.product_id
#WHERE o.order_date = (
#    SELECT MAX(o2.order_date)
#    FROM Orders o2
#    WHERE o2.product_id = p.product_id
#)
#ORDER BY p.product_name, p.product_id, o.order_id;
#
#-- Alternative with RANK():
#-- WITH RankedOrders AS (
#--     SELECT o.*, p.product_name,
#--            RANK() OVER (PARTITION BY o.product_id ORDER BY o.order_date DESC) as rk
#--     FROM Orders o
#--     JOIN Products p ON o.product_id = p.product_id
#-- )
#-- SELECT product_name, product_id, order_id, order_date
#-- FROM RankedOrders
#-- WHERE rk = 1
#-- ORDER BY product_name, product_id, order_id;

from typing import List
from collections import defaultdict

class Solution:
    def mostRecentOrdersForEachProduct(
        self,
        customers: List[dict],
        orders: List[dict],
        products: List[dict]
    ) -> List[dict]:
        """
        Python simulation: Find most recent order(s) for each product.
        """
        # Build product lookup
        product_map = {p['product_id']: p['product_name'] for p in products}

        # Group orders by product
        product_orders = defaultdict(list)
        for order in orders:
            pid = order['product_id']
            if pid in product_map:
                product_orders[pid].append(order)

        result = []

        for pid, porders in product_orders.items():
            if not porders:
                continue

            # Find max date
            max_date = max(o['order_date'] for o in porders)

            # Get all orders with max date
            for order in porders:
                if order['order_date'] == max_date:
                    result.append({
                        'product_name': product_map[pid],
                        'product_id': pid,
                        'order_id': order['order_id'],
                        'order_date': order['order_date']
                    })

        # Sort by product_name, product_id, order_id
        result.sort(key=lambda x: (x['product_name'], x['product_id'], x['order_id']))

        return result


class SolutionGroupBy:
    def mostRecentOrdersForEachProduct(
        self,
        customers: List[dict],
        orders: List[dict],
        products: List[dict]
    ) -> List[dict]:
        """
        Using groupby and max.
        """
        from itertools import groupby

        product_map = {p['product_id']: p['product_name'] for p in products}

        # Filter and group orders
        valid_orders = [o for o in orders if o['product_id'] in product_map]
        valid_orders.sort(key=lambda x: x['product_id'])

        result = []

        for pid, group in groupby(valid_orders, key=lambda x: x['product_id']):
            group_list = list(group)
            max_date = max(o['order_date'] for o in group_list)

            for order in group_list:
                if order['order_date'] == max_date:
                    result.append({
                        'product_name': product_map[pid],
                        'product_id': pid,
                        'order_id': order['order_id'],
                        'order_date': order['order_date']
                    })

        result.sort(key=lambda x: (x['product_name'], x['product_id'], x['order_id']))
        return result


class SolutionOnePass:
    def mostRecentOrdersForEachProduct(
        self,
        customers: List[dict],
        orders: List[dict],
        products: List[dict]
    ) -> List[dict]:
        """
        Single pass to find max dates and collect orders.
        """
        product_map = {p['product_id']: p['product_name'] for p in products}

        # Track max date and orders for each product
        max_dates = {}
        product_orders = defaultdict(list)

        for order in orders:
            pid = order['product_id']
            if pid not in product_map:
                continue

            date = order['order_date']

            if pid not in max_dates or date > max_dates[pid]:
                max_dates[pid] = date
                product_orders[pid] = [order]
            elif date == max_dates[pid]:
                product_orders[pid].append(order)

        result = []
        for pid, porders in product_orders.items():
            for order in porders:
                result.append({
                    'product_name': product_map[pid],
                    'product_id': pid,
                    'order_id': order['order_id'],
                    'order_date': order['order_date']
                })

        result.sort(key=lambda x: (x['product_name'], x['product_id'], x['order_id']))
        return result
