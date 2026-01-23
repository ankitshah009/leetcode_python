#1511. Customer Order Frequency
#Easy (SQL)
#
#Table: Customers
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| customer_id   | int     |
#| name          | varchar |
#| country       | varchar |
#+---------------+---------+
#customer_id is the primary key for this table.
#This table contains information about the customers in the company.
#
#Table: Product
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| description   | varchar |
#| price         | int     |
#+---------------+---------+
#product_id is the primary key for this table.
#This table contains information on the products in the company.
#price is the product cost.
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| customer_id   | int     |
#| product_id    | int     |
#| order_date    | date    |
#| quantity      | int     |
#+---------------+---------+
#order_id is the primary key for this table.
#This table contains information on customer orders.
#customer_id is the id of the customer who bought "quantity" products with id
#"product_id". Order_date is the date in format ('YYYY-MM-DD') when the order
#was shipped.
#
#Write an SQL query to report the customer_id and customer_name of customers
#who have spent at least $100 in each month of June and July 2020.
#
#Return the result table in any order.

#SQL Solution:
#SELECT c.customer_id, c.name
#FROM Customers c
#WHERE c.customer_id IN (
#    SELECT o.customer_id
#    FROM Orders o
#    JOIN Product p ON o.product_id = p.product_id
#    WHERE o.order_date BETWEEN '2020-06-01' AND '2020-06-30'
#    GROUP BY o.customer_id
#    HAVING SUM(o.quantity * p.price) >= 100
#)
#AND c.customer_id IN (
#    SELECT o.customer_id
#    FROM Orders o
#    JOIN Product p ON o.product_id = p.product_id
#    WHERE o.order_date BETWEEN '2020-07-01' AND '2020-07-31'
#    GROUP BY o.customer_id
#    HAVING SUM(o.quantity * p.price) >= 100
#);

from typing import List
from collections import defaultdict
from datetime import datetime

class Solution:
    def customerOrderFrequency(self, customers: List[dict], products: List[dict],
                               orders: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Find customers who spent >= $100 in both June 2020 and July 2020.
        """
        # Product price lookup
        product_price = {p['product_id']: p['price'] for p in products}

        # Customer info lookup
        customer_info = {c['customer_id']: c['name'] for c in customers}

        # Calculate monthly spending per customer
        monthly_spending = defaultdict(lambda: defaultdict(int))

        for order in orders:
            date = order['order_date']
            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d')

            year_month = (date.year, date.month)
            customer_id = order['customer_id']
            product_id = order['product_id']
            quantity = order['quantity']

            price = product_price.get(product_id, 0)
            monthly_spending[customer_id][year_month] += quantity * price

        # Find customers meeting criteria
        result = []
        for customer_id, spending in monthly_spending.items():
            june_2020 = spending.get((2020, 6), 0)
            july_2020 = spending.get((2020, 7), 0)

            if june_2020 >= 100 and july_2020 >= 100:
                result.append({
                    'customer_id': customer_id,
                    'name': customer_info.get(customer_id)
                })

        return result


class SolutionExplicit:
    def customerOrderFrequency(self, customers: List[dict], products: List[dict],
                               orders: List[dict]) -> List[dict]:
        """More explicit step-by-step solution"""
        # Step 1: Build lookup tables
        product_price = {p['product_id']: p['price'] for p in products}
        customer_name = {c['customer_id']: c['name'] for c in customers}

        # Step 2: Calculate June 2020 spending
        june_spending = defaultdict(int)
        for order in orders:
            date = order['order_date']
            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d')

            if date.year == 2020 and date.month == 6:
                customer_id = order['customer_id']
                total = order['quantity'] * product_price.get(order['product_id'], 0)
                june_spending[customer_id] += total

        # Step 3: Calculate July 2020 spending
        july_spending = defaultdict(int)
        for order in orders:
            date = order['order_date']
            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d')

            if date.year == 2020 and date.month == 7:
                customer_id = order['customer_id']
                total = order['quantity'] * product_price.get(order['product_id'], 0)
                july_spending[customer_id] += total

        # Step 4: Find customers meeting both criteria
        result = []
        for customer_id in customer_name:
            if june_spending[customer_id] >= 100 and july_spending[customer_id] >= 100:
                result.append({
                    'customer_id': customer_id,
                    'name': customer_name[customer_id]
                })

        return result
