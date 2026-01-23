#1445. Apples & Oranges
#Medium
#
#Table: Sales
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| sale_date     | date    |
#| fruit         | enum    |
#| sold_num      | int     |
#+---------------+---------+
#(sale_date, fruit) is the primary key for this table.
#This table contains the sales of "apples" and "oranges" sold each day.
#
#Write an SQL query to report the difference between the number of apples and
#oranges sold each day.
#
#Return the result table ordered by sale_date.
#
#Example 1:
#Input:
#Sales table:
#+------------+------------+-------------+
#| sale_date  | fruit      | sold_num    |
#+------------+------------+-------------+
#| 2020-05-01 | apples     | 10          |
#| 2020-05-01 | oranges    | 8           |
#| 2020-05-02 | apples     | 15          |
#| 2020-05-02 | oranges    | 15          |
#| 2020-05-03 | apples     | 20          |
#| 2020-05-03 | oranges    | 0           |
#| 2020-05-04 | apples     | 15          |
#| 2020-05-04 | oranges    | 16          |
#+------------+------------+-------------+
#Output:
#+------------+--------------+
#| sale_date  | diff         |
#+------------+--------------+
#| 2020-05-01 | 2            |
#| 2020-05-02 | 0            |
#| 2020-05-03 | 20           |
#| 2020-05-04 | -1           |
#+------------+--------------+
#Explanation:
#Day 2020-05-01, 10 apples and 8 oranges were sold (Difference  10 - 8 = 2).
#Day 2020-05-02, 15 apples and 15 oranges were sold (Difference 15 - 15 = 0).
#Day 2020-05-03, 20 apples and 0 oranges were sold (Difference 20 - 0 = 20).
#Day 2020-05-04, 15 apples and 16 oranges were sold (Difference 15 - 16 = -1).

#SQL Solution:
#SELECT
#    sale_date,
#    SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END) AS diff
#FROM Sales
#GROUP BY sale_date
#ORDER BY sale_date;

#Alternative SQL using self-join:
#SELECT
#    a.sale_date,
#    a.sold_num - o.sold_num AS diff
#FROM Sales a
#JOIN Sales o ON a.sale_date = o.sale_date
#WHERE a.fruit = 'apples' AND o.fruit = 'oranges'
#ORDER BY a.sale_date;

from typing import List
from collections import defaultdict

class Solution:
    def applesAndOranges(self, sales: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Calculate difference (apples - oranges) for each day.
        """
        # Group by date
        daily_sales = defaultdict(lambda: {'apples': 0, 'oranges': 0})

        for sale in sales:
            date = sale['sale_date']
            fruit = sale['fruit']
            daily_sales[date][fruit] = sale['sold_num']

        # Calculate differences
        result = []
        for date in sorted(daily_sales.keys()):
            diff = daily_sales[date]['apples'] - daily_sales[date]['oranges']
            result.append({'sale_date': date, 'diff': diff})

        return result


class SolutionSinglePass:
    def applesAndOranges(self, sales: List[dict]) -> List[dict]:
        """Single pass through sales"""
        diff_by_date = defaultdict(int)

        for sale in sales:
            date = sale['sale_date']
            amount = sale['sold_num']
            if sale['fruit'] == 'apples':
                diff_by_date[date] += amount
            else:
                diff_by_date[date] -= amount

        return [{'sale_date': date, 'diff': diff}
                for date, diff in sorted(diff_by_date.items())]
