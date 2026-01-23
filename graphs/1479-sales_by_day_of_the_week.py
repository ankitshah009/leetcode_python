#1479. Sales by Day of the Week
#Hard (SQL)
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| customer_id   | int     |
#| order_date    | date    |
#| item_id       | int     |
#| quantity      | int     |
#+---------------+---------+
#(order_id, item_id) is the primary key for this table.
#This table contains information on the orders placed.
#order_date is the date item_id was ordered by customer_id.
#
#Table: Items
#+---------------------+---------+
#| Column Name         | Type    |
#+---------------------+---------+
#| item_id             | int     |
#| item_name           | varchar |
#| item_category       | varchar |
#+---------------------+---------+
#item_id is the primary key for this table.
#item_name is the name of the item.
#item_category is the category of the item.
#
#Write an SQL query to report how many units in each category have been ordered
#on each day of the week.
#
#Return the result table ordered by category.
#
#Example 1:
#Input:
#Orders table:
#+------------+--------------+-------------+-----------+----------+
#| order_id   | customer_id  | order_date  | item_id   | quantity |
#+------------+--------------+-------------+-----------+----------+
#| 1          | 1            | 2020-06-01  | 1         | 10       |
#| 2          | 1            | 2020-06-08  | 2         | 10       |
#| 3          | 2            | 2020-06-02  | 1         | 5        |
#| 4          | 3            | 2020-06-03  | 3         | 5        |
#| 5          | 4            | 2020-06-04  | 4         | 1        |
#| 6          | 4            | 2020-06-05  | 5         | 5        |
#| 7          | 5            | 2020-06-05  | 1         | 10       |
#| 8          | 5            | 2020-06-14  | 4         | 5        |
#| 9          | 5            | 2020-06-21  | 3         | 5        |
#+------------+--------------+-------------+-----------+----------+
#
#Items table:
#+----------+----------------+---------------+
#| item_id  | item_name      | item_category |
#+----------+----------------+---------------+
#| 1        | LC Alg. Book   | Book          |
#| 2        | LC DB. Book    | Book          |
#| 3        | LC SmarthPhone | Phone         |
#| 4        | LC Phone 2020  | Phone         |
#| 5        | LC Notes       | Phone         |
#+----------+----------------+---------------+
#
#Output:
#+----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
#| Category | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Saturday  | Sunday    |
#+----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
#| Book     | 20        | 5         | 0         | 0         | 10        | 0         | 0         |
#| Phone    | 0         | 0         | 5         | 1         | 0         | 0         | 10        |
#+----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

#SQL Solution:
#SELECT
#    i.item_category AS Category,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 2 THEN o.quantity END), 0) AS Monday,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 3 THEN o.quantity END), 0) AS Tuesday,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 4 THEN o.quantity END), 0) AS Wednesday,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 5 THEN o.quantity END), 0) AS Thursday,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 6 THEN o.quantity END), 0) AS Friday,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 7 THEN o.quantity END), 0) AS Saturday,
#    COALESCE(SUM(CASE WHEN DAYOFWEEK(o.order_date) = 1 THEN o.quantity END), 0) AS Sunday
#FROM Items i
#LEFT JOIN Orders o ON i.item_id = o.item_id
#GROUP BY i.item_category
#ORDER BY i.item_category;

from typing import List
from collections import defaultdict
from datetime import datetime

class Solution:
    def salesByDayOfWeek(self, orders: List[dict], items: List[dict]) -> List[dict]:
        """
        Python simulation of SQL pivot table query.
        """
        # Create item_id -> category mapping
        item_category = {item['item_id']: item['item_category'] for item in items}

        # Get all categories
        categories = sorted(set(item['item_category'] for item in items))

        # Initialize result
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        sales = {cat: {day: 0 for day in day_names} for cat in categories}

        # Process orders
        for order in orders:
            item_id = order['item_id']
            quantity = order['quantity']
            order_date = order['order_date']

            # Get day of week (0 = Monday in Python)
            if isinstance(order_date, str):
                order_date = datetime.strptime(order_date, '%Y-%m-%d')
            day_idx = order_date.weekday()
            day_name = day_names[day_idx]

            category = item_category.get(item_id)
            if category:
                sales[category][day_name] += quantity

        # Format result
        result = []
        for cat in categories:
            row = {'Category': cat}
            for day in day_names:
                row[day] = sales[cat][day]
            result.append(row)

        return result


class SolutionExplicit:
    def salesByDayOfWeek(self, orders: List[dict], items: List[dict]) -> List[dict]:
        """More explicit step-by-step solution"""
        # Step 1: Create lookup tables
        item_to_category = {}
        all_categories = set()

        for item in items:
            item_to_category[item['item_id']] = item['item_category']
            all_categories.add(item['item_category'])

        # Step 2: Initialize sales tracking
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        category_sales = defaultdict(lambda: defaultdict(int))

        # Step 3: Aggregate orders
        for order in orders:
            item_id = order['item_id']
            if item_id not in item_to_category:
                continue

            category = item_to_category[item_id]
            quantity = order['quantity']
            date = order['order_date']

            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d')

            day_of_week = day_order[date.weekday()]
            category_sales[category][day_of_week] += quantity

        # Step 4: Build result with all categories (even those with no orders)
        result = []
        for category in sorted(all_categories):
            row = {'Category': category}
            for day in day_order:
                row[day] = category_sales[category][day]
            result.append(row)

        return result
