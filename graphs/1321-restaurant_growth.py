#1321. Restaurant Growth
#Medium
#
#Table: Customer
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| customer_id   | int     |
#| name          | varchar |
#| visited_on    | date    |
#| amount        | int     |
#+---------------+---------+
#(customer_id, visited_on) is the primary key for this table.
#This table contains data about customer transactions in a restaurant.
#visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
#amount is the total paid by a customer.
#
#You are the restaurant owner and you want to analyze a possible expansion.
#
#Compute the moving average of how much the customer paid in a seven days window
#(i.e., current day + 6 days before). average_amount should be rounded to two
#decimal places.
#
#Return the result table ordered by visited_on in ascending order.
#The result format is in the following example.
#
#Example 1:
#Input:
#Customer table:
#+-------------+--------------+--------------+-------------+
#| customer_id | name         | visited_on   | amount      |
#+-------------+--------------+--------------+-------------+
#| 1           | Jhon         | 2019-01-01   | 100         |
#| 2           | Daniel       | 2019-01-02   | 110         |
#| 3           | Jade         | 2019-01-03   | 120         |
#| 4           | Khaled       | 2019-01-04   | 130         |
#| 5           | Winston      | 2019-01-05   | 110         |
#| 6           | Elvis        | 2019-01-06   | 140         |
#| 7           | Anna         | 2019-01-07   | 150         |
#| 8           | Maria        | 2019-01-08   | 80          |
#| 9           | Jaze         | 2019-01-09   | 110         |
#| 1           | Jhon         | 2019-01-10   | 130         |
#| 3           | Jade         | 2019-01-10   | 150         |
#+-------------+--------------+--------------+-------------+
#Output:
#+--------------+--------------+----------------+
#| visited_on   | amount       | average_amount |
#+--------------+--------------+----------------+
#| 2019-01-07   | 860          | 122.86         |
#| 2019-01-08   | 840          | 120.00         |
#| 2019-01-09   | 840          | 120.00         |
#| 2019-01-10   | 1000         | 142.86         |
#+--------------+--------------+----------------+

# SQL Solution:
# SELECT
#     visited_on,
#     amount,
#     ROUND(amount / 7.0, 2) AS average_amount
# FROM (
#     SELECT
#         visited_on,
#         SUM(amount) OVER (
#             ORDER BY visited_on
#             RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
#         ) AS amount,
#         DENSE_RANK() OVER (ORDER BY visited_on) AS rk
#     FROM (
#         SELECT visited_on, SUM(amount) AS amount
#         FROM Customer
#         GROUP BY visited_on
#     ) daily
# ) t
# WHERE rk >= 7
# ORDER BY visited_on;

# Alternative SQL:
# SELECT
#     c1.visited_on,
#     SUM(c2.amount) AS amount,
#     ROUND(SUM(c2.amount) / 7.0, 2) AS average_amount
# FROM (
#     SELECT visited_on, SUM(amount) AS amount
#     FROM Customer
#     GROUP BY visited_on
# ) c1
# JOIN (
#     SELECT visited_on, SUM(amount) AS amount
#     FROM Customer
#     GROUP BY visited_on
# ) c2
# ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
# GROUP BY c1.visited_on
# HAVING COUNT(DISTINCT c2.visited_on) = 7
# ORDER BY c1.visited_on;

# Python simulation
from typing import List, Tuple
from datetime import date, timedelta
from collections import defaultdict

class Solution:
    def restaurantGrowth(
        self,
        customers: List[Tuple[int, str, date, int]]
    ) -> List[Tuple[date, int, float]]:
        """
        Calculate 7-day rolling sum and average.
        """
        # Aggregate by date
        daily = defaultdict(int)
        for customer_id, name, visited_on, amount in customers:
            daily[visited_on] += amount

        # Get sorted dates
        dates = sorted(daily.keys())

        if len(dates) < 7:
            return []

        result = []

        # Sliding window of 7 days
        window_sum = sum(daily[dates[i]] for i in range(7))

        result.append((dates[6], window_sum, round(window_sum / 7, 2)))

        for i in range(7, len(dates)):
            # Check if consecutive days for proper window
            window_dates = []
            for d in dates:
                if dates[i] - timedelta(days=6) <= d <= dates[i]:
                    window_dates.append(d)

            if len(window_dates) == 7:
                window_sum = sum(daily[d] for d in window_dates)
                result.append((dates[i], window_sum, round(window_sum / 7, 2)))

        return result
