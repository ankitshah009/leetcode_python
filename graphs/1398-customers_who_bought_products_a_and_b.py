#1398. Customers Who Bought Products A and B but Not C
#Medium
#
#Table: Customers
#+---------------------+---------+
#| Column Name         | Type    |
#+---------------------+---------+
#| customer_id         | int     |
#| customer_name       | varchar |
#+---------------------+---------+
#customer_id is the primary key for this table.
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| customer_id   | int     |
#| product_name  | varchar |
#+---------------+---------+
#order_id is the primary key for this table.
#customer_id is a foreign key to Customers table.
#
#Write an SQL query to report the customer_id and customer_name of customers
#who bought products "A", "B" but did not buy the product "C" since we want to
#recommend them to purchase this product.
#
#Return the result table ordered by customer_id.
#
#Example 1:
#Input:
#Customers table:
#+-------------+---------------+
#| customer_id | customer_name |
#+-------------+---------------+
#| 1           | Daniel        |
#| 2           | Diana         |
#| 3           | Elizabeth     |
#| 4           | Jhon          |
#+-------------+---------------+
#Orders table:
#+------------+--------------+---------------+
#| order_id   | customer_id  | product_name  |
#+------------+--------------+---------------+
#| 10         | 1            | A             |
#| 20         | 1            | B             |
#| 30         | 1            | D             |
#| 40         | 1            | C             |
#| 50         | 2            | A             |
#| 60         | 3            | A             |
#| 70         | 3            | B             |
#| 80         | 3            | D             |
#| 90         | 4            | C             |
#+------------+--------------+---------------+
#Output:
#+-------------+---------------+
#| customer_id | customer_name |
#+-------------+---------------+
#| 3           | Elizabeth     |
#+-------------+---------------+
#Explanation: Only customer 3 bought A and B but not C.

#SQL Solution:
#SELECT c.customer_id, c.customer_name
#FROM Customers c
#WHERE c.customer_id IN (
#    SELECT customer_id FROM Orders WHERE product_name = 'A'
#)
#AND c.customer_id IN (
#    SELECT customer_id FROM Orders WHERE product_name = 'B'
#)
#AND c.customer_id NOT IN (
#    SELECT customer_id FROM Orders WHERE product_name = 'C'
#)
#ORDER BY c.customer_id;

#Alternative SQL using GROUP BY and HAVING:
#SELECT c.customer_id, c.customer_name
#FROM Customers c
#JOIN Orders o ON c.customer_id = o.customer_id
#GROUP BY c.customer_id, c.customer_name
#HAVING SUM(product_name = 'A') > 0
#   AND SUM(product_name = 'B') > 0
#   AND SUM(product_name = 'C') = 0
#ORDER BY c.customer_id;

from typing import List
from collections import defaultdict

class Solution:
    def customersWhoBoughtAAndBButNotC(
        self, customers: List[dict], orders: List[dict]
    ) -> List[dict]:
        """
        Python simulation of SQL query.
        Find customers who bought A and B but not C.
        """
        # Build customer products mapping
        customer_products = defaultdict(set)
        for order in orders:
            customer_id = order['customer_id']
            product = order['product_name']
            customer_products[customer_id].add(product)

        # Build customer names mapping
        customer_names = {c['customer_id']: c['customer_name'] for c in customers}

        # Filter customers
        result = []
        for customer_id, products in customer_products.items():
            if 'A' in products and 'B' in products and 'C' not in products:
                result.append({
                    'customer_id': customer_id,
                    'customer_name': customer_names[customer_id]
                })

        # Sort by customer_id
        result.sort(key=lambda x: x['customer_id'])

        return result


class SolutionExplicit:
    def customersWhoBoughtAAndBButNotC(
        self, customers: List[dict], orders: List[dict]
    ) -> List[dict]:
        """More explicit tracking"""
        bought_a = set()
        bought_b = set()
        bought_c = set()

        for order in orders:
            cid = order['customer_id']
            product = order['product_name']

            if product == 'A':
                bought_a.add(cid)
            elif product == 'B':
                bought_b.add(cid)
            elif product == 'C':
                bought_c.add(cid)

        # Find customers who bought A and B but not C
        target_customers = (bought_a & bought_b) - bought_c

        # Get names
        customer_names = {c['customer_id']: c['customer_name'] for c in customers}

        result = [
            {'customer_id': cid, 'customer_name': customer_names[cid]}
            for cid in sorted(target_customers)
        ]

        return result
