#1607. Sellers With No Sales
#Easy (SQL)
#
#Table: Customer
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| customer_id   | int     |
#| customer_name | varchar |
#+---------------+---------+
#customer_id is the primary key for this table.
#Each row of this table contains the information of each customer.
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| sale_date     | date    |
#| order_cost    | int     |
#| customer_id   | int     |
#| seller_id     | int     |
#+---------------+---------+
#order_id is the primary key for this table.
#Each row of this table contains all orders made in the market.
#seller_id is a foreign key to the Seller table.
#customer_id is a foreign key to the Customer table.
#
#Table: Seller
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| seller_id     | int     |
#| seller_name   | varchar |
#+---------------+---------+
#seller_id is the primary key for this table.
#Each row of this table contains the information of each seller.
#
#Write an SQL query to report the names of all sellers who did not make any
#sales in 2020.
#
#Return the result table ordered by seller_name in ascending order.
#
#Example 1:
#Input:
#Customer table:
#+-------------+---------------+
#| customer_id | customer_name |
#+-------------+---------------+
#| 101         | Alice         |
#| 102         | Bob           |
#| 103         | Charlie       |
#+-------------+---------------+
#
#Orders table:
#+----------+------------+------------+-------------+-----------+
#| order_id | sale_date  | order_cost | customer_id | seller_id |
#+----------+------------+------------+-------------+-----------+
#| 1        | 2020-03-01 | 1500       | 101         | 1         |
#| 2        | 2020-05-25 | 2400       | 102         | 2         |
#| 3        | 2019-05-25 | 800        | 101         | 3         |
#| 4        | 2020-09-13 | 1000       | 103         | 2         |
#| 5        | 2019-02-11 | 700        | 101         | 2         |
#+----------+------------+------------+-------------+-----------+
#
#Seller table:
#+-----------+-------------+
#| seller_id | seller_name |
#+-----------+-------------+
#| 1         | Daniel      |
#| 2         | Elizabeth   |
#| 3         | Frank       |
#+-----------+-------------+
#
#Output:
#+-------------+
#| seller_name |
#+-------------+
#| Frank       |
#+-------------+
#Explanation: Frank made 1 sale in 2019 but no sales in 2020.

#SQL Solution:
#SELECT seller_name
#FROM Seller
#WHERE seller_id NOT IN (
#    SELECT DISTINCT seller_id
#    FROM Orders
#    WHERE YEAR(sale_date) = 2020
#)
#ORDER BY seller_name;
#
#-- Alternative using LEFT JOIN:
#-- SELECT s.seller_name
#-- FROM Seller s
#-- LEFT JOIN Orders o ON s.seller_id = o.seller_id AND YEAR(o.sale_date) = 2020
#-- WHERE o.order_id IS NULL
#-- ORDER BY s.seller_name;

from typing import List, Dict
from collections import defaultdict

class Solution:
    def sellersWithNoSales(
        self,
        sellers: List[Dict],
        orders: List[Dict]
    ) -> List[str]:
        """
        Python simulation: Find sellers with no sales in 2020.
        """
        # Find sellers who made sales in 2020
        sellers_with_2020_sales = set()

        for order in orders:
            year = order['sale_date'].year if hasattr(order['sale_date'], 'year') else int(order['sale_date'][:4])
            if year == 2020:
                sellers_with_2020_sales.add(order['seller_id'])

        # Find sellers without 2020 sales
        result = []
        for seller in sellers:
            if seller['seller_id'] not in sellers_with_2020_sales:
                result.append(seller['seller_name'])

        return sorted(result)


class SolutionLeftJoin:
    def sellersWithNoSales(
        self,
        sellers: List[Dict],
        orders: List[Dict]
    ) -> List[str]:
        """
        Simulate LEFT JOIN approach.
        """
        # Build set of sellers with 2020 orders
        def get_year(date_str):
            if isinstance(date_str, str):
                return int(date_str.split('-')[0])
            return date_str.year

        active_2020 = {
            o['seller_id']
            for o in orders
            if get_year(o['sale_date']) == 2020
        }

        # Return sellers not in active_2020
        result = [
            s['seller_name']
            for s in sellers
            if s['seller_id'] not in active_2020
        ]

        return sorted(result)
