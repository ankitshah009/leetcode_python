#1565. Unique Orders and Customers Per Month
#Easy (SQL)
#
#Table: Orders
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| order_id      | int     |
#| order_date    | date    |
#| customer_id   | int     |
#| invoice       | int     |
#+---------------+---------+
#order_id is the primary key for this table.
#This table contains information about the orders made by customer_id.
#
#Write an SQL query to find the number of unique orders and the number of unique
#customers with invoices > $20 for each different month.
#
#Return the result table sorted by month in any order.
#
#Example 1:
#Input:
#Orders table:
#+----------+------------+-------------+----------+
#| order_id | order_date | customer_id | invoice  |
#+----------+------------+-------------+----------+
#| 1        | 2020-09-15 | 1           | 30       |
#| 2        | 2020-09-17 | 2           | 90       |
#| 3        | 2020-10-06 | 3           | 20       |
#| 4        | 2020-10-20 | 3           | 21       |
#| 5        | 2020-11-10 | 1           | 10       |
#| 6        | 2020-11-21 | 2           | 15       |
#| 7        | 2020-12-01 | 4           | 55       |
#| 8        | 2020-12-03 | 4           | 77       |
#+----------+------------+-------------+----------+
#
#Output:
#+---------+-------------+----------------+
#| month   | order_count | customer_count |
#+---------+-------------+----------------+
#| 2020-09 | 2           | 2              |
#| 2020-10 | 1           | 1              |
#| 2020-12 | 2           | 1              |
#+---------+-------------+----------------+

#SQL Solution:
#SELECT
#    DATE_FORMAT(order_date, '%Y-%m') AS month,
#    COUNT(DISTINCT order_id) AS order_count,
#    COUNT(DISTINCT customer_id) AS customer_count
#FROM Orders
#WHERE invoice > 20
#GROUP BY DATE_FORMAT(order_date, '%Y-%m')
#ORDER BY month;

from typing import List
from collections import defaultdict

class Solution:
    def uniqueOrdersAndCustomersPerMonth(self, orders: List[dict]) -> List[dict]:
        """
        Python simulation: Group by month, count unique orders and customers.
        """
        # Filter orders with invoice > 20
        filtered = [o for o in orders if o['invoice'] > 20]

        # Group by month
        monthly_data = defaultdict(lambda: {'orders': set(), 'customers': set()})

        for order in filtered:
            date = order['order_date']
            month = date[:7] if isinstance(date, str) else date.strftime('%Y-%m')

            monthly_data[month]['orders'].add(order['order_id'])
            monthly_data[month]['customers'].add(order['customer_id'])

        # Build result
        result = []
        for month, data in monthly_data.items():
            result.append({
                'month': month,
                'order_count': len(data['orders']),
                'customer_count': len(data['customers'])
            })

        result.sort(key=lambda x: x['month'])
        return result


class SolutionCounter:
    def uniqueOrdersAndCustomersPerMonth(self, orders: List[dict]) -> List[dict]:
        """
        Using sets for counting.
        """
        monthly_orders = defaultdict(set)
        monthly_customers = defaultdict(set)

        for order in orders:
            if order['invoice'] > 20:
                date = order['order_date']
                month = date[:7] if isinstance(date, str) else date.strftime('%Y-%m')

                monthly_orders[month].add(order['order_id'])
                monthly_customers[month].add(order['customer_id'])

        result = [
            {
                'month': month,
                'order_count': len(monthly_orders[month]),
                'customer_count': len(monthly_customers[month])
            }
            for month in monthly_orders
        ]

        return sorted(result, key=lambda x: x['month'])


class SolutionGroupBy:
    def uniqueOrdersAndCustomersPerMonth(self, orders: List[dict]) -> List[dict]:
        """
        Using itertools.groupby.
        """
        from itertools import groupby

        # Filter and extract month
        filtered = [
            {
                'month': o['order_date'][:7] if isinstance(o['order_date'], str)
                         else o['order_date'].strftime('%Y-%m'),
                'order_id': o['order_id'],
                'customer_id': o['customer_id']
            }
            for o in orders
            if o['invoice'] > 20
        ]

        # Sort by month for groupby
        filtered.sort(key=lambda x: x['month'])

        result = []
        for month, group in groupby(filtered, key=lambda x: x['month']):
            group_list = list(group)
            result.append({
                'month': month,
                'order_count': len(set(o['order_id'] for o in group_list)),
                'customer_count': len(set(o['customer_id'] for o in group_list))
            })

        return result
