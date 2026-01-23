#1327. List the Products Ordered in a Period
#Easy
#
#Table: Products
#+------------------+---------+
#| Column Name      | Type    |
#+------------------+---------+
#| product_id       | int     |
#| product_name     | varchar |
#| product_category | varchar |
#+------------------+---------+
#product_id is the primary key for this table.
#This table contains data about the company's products.
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| order_date    | date    |
#| unit          | int     |
#+---------------+---------+
#There is no primary key for this table. It may have duplicate rows.
#product_id is a foreign key to the Products table.
#unit is the number of products ordered in order_date.
#
#Write an SQL query to get the names of products that have at least 100 units
#ordered in February 2020 and their amount.
#
#Return result table in any order.
#
#Example 1:
#Input:
#Products table:
#+-------------+-----------------------+------------------+
#| product_id  | product_name          | product_category |
#+-------------+-----------------------+------------------+
#| 1           | Leetcode Solutions    | Book             |
#| 2           | Jewels of Stringology | Book             |
#| 3           | HP                    | Laptop           |
#| 4           | Lenovo                | Laptop           |
#| 5           | Leetcode Kit          | T-shirt          |
#+-------------+-----------------------+------------------+
#Orders table:
#+------------+--------------+----------+
#| product_id | order_date   | unit     |
#+------------+--------------+----------+
#| 1          | 2020-02-05   | 60       |
#| 1          | 2020-02-10   | 70       |
#| 2          | 2020-01-18   | 30       |
#| 2          | 2020-02-11   | 80       |
#| 3          | 2020-02-17   | 2        |
#| 3          | 2020-02-24   | 3        |
#| 4          | 2020-03-01   | 20       |
#| 4          | 2020-03-04   | 30       |
#| 4          | 2020-03-05   | 60       |
#| 5          | 2020-02-25   | 50       |
#| 5          | 2020-02-27   | 50       |
#| 5          | 2020-03-01   | 50       |
#+------------+--------------+----------+
#Output:
#+--------------------+---------+
#| product_name       | unit    |
#+--------------------+---------+
#| Leetcode Solutions | 130     |
#| Leetcode Kit       | 100     |
#+--------------------+---------+

# SQL Solution:
# SELECT p.product_name, SUM(o.unit) AS unit
# FROM Products p
# JOIN Orders o ON p.product_id = o.product_id
# WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
# GROUP BY p.product_id, p.product_name
# HAVING SUM(o.unit) >= 100;

# Alternative using YEAR and MONTH:
# SELECT p.product_name, SUM(o.unit) AS unit
# FROM Products p
# JOIN Orders o ON p.product_id = o.product_id
# WHERE YEAR(o.order_date) = 2020 AND MONTH(o.order_date) = 2
# GROUP BY p.product_id, p.product_name
# HAVING SUM(o.unit) >= 100;

# Python simulation
from typing import List, Tuple
from datetime import date
from collections import defaultdict

class Solution:
    def productsOrdered(
        self,
        products: List[Tuple[int, str, str]],
        orders: List[Tuple[int, date, int]]
    ) -> List[Tuple[str, int]]:
        """
        Find products with at least 100 units ordered in Feb 2020.
        """
        # Create product name mapping
        product_names = {pid: name for pid, name, _ in products}

        # Sum units for Feb 2020
        feb_units = defaultdict(int)
        for product_id, order_date, unit in orders:
            if order_date.year == 2020 and order_date.month == 2:
                feb_units[product_id] += unit

        # Filter products with >= 100 units
        result = []
        for product_id, total in feb_units.items():
            if total >= 100:
                result.append((product_names[product_id], total))

        return result
