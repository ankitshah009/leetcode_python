#1384. Total Sales Amount by Year
#Hard
#
#Table: Product
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| product_name  | varchar |
#+---------------+---------+
#product_id is the primary key for this table.
#
#Table: Sales
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| period_start  | date    |
#| period_end    | date    |
#| average_daily_sales | int |
#+---------------+---------+
#product_id is the primary key for this table.
#
#Write an SQL query to report the total sales amount of each item for each year.
#Return the result table ordered by product_id, report_year.
#
#Example 1:
#Input:
#Product table:
#+------------+--------------+
#| product_id | product_name |
#+------------+--------------+
#| 1          | LC Phone     |
#| 2          | LC T-Shirt   |
#| 3          | LC Keychain  |
#+------------+--------------+
#Sales table:
#+------------+--------------+-------------+---------------------+
#| product_id | period_start | period_end  | average_daily_sales |
#+------------+--------------+-------------+---------------------+
#| 1          | 2019-01-25   | 2019-02-28  | 100                 |
#| 2          | 2018-12-01   | 2020-01-01  | 10                  |
#| 3          | 2019-12-01   | 2020-01-31  | 1                   |
#+------------+--------------+-------------+---------------------+
#Output:
#+------------+--------------+-------------+--------------+
#| product_id | product_name | report_year | total_amount |
#+------------+--------------+-------------+--------------+
#| 1          | LC Phone     | 2019        | 3500         |
#| 2          | LC T-Shirt   | 2018        | 310          |
#| 2          | LC T-Shirt   | 2019        | 3650         |
#| 2          | LC T-Shirt   | 2020        | 10           |
#| 3          | LC Keychain  | 2019        | 31           |
#| 3          | LC Keychain  | 2020        | 31           |
#+------------+--------------+-------------+--------------+

#SQL Solution:
#WITH RECURSIVE years AS (
#    SELECT MIN(YEAR(period_start)) as year FROM Sales
#    UNION ALL
#    SELECT year + 1 FROM years WHERE year < (SELECT MAX(YEAR(period_end)) FROM Sales)
#)
#SELECT
#    s.product_id,
#    p.product_name,
#    CAST(y.year AS CHAR) as report_year,
#    s.average_daily_sales * (
#        DATEDIFF(
#            LEAST(s.period_end, CONCAT(y.year, '-12-31')),
#            GREATEST(s.period_start, CONCAT(y.year, '-01-01'))
#        ) + 1
#    ) as total_amount
#FROM Sales s
#JOIN Product p ON s.product_id = p.product_id
#JOIN years y ON y.year BETWEEN YEAR(s.period_start) AND YEAR(s.period_end)
#ORDER BY s.product_id, report_year;

from typing import List
from datetime import date, timedelta
from collections import defaultdict

class Solution:
    def totalSalesAmountByYear(self, products: List[dict], sales: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Expand each sale period into yearly amounts.
        """
        product_names = {p['product_id']: p['product_name'] for p in products}

        result = []

        for sale in sales:
            product_id = sale['product_id']
            period_start = sale['period_start']
            period_end = sale['period_end']
            daily_sales = sale['average_daily_sales']

            # Get years covered
            start_year = period_start.year
            end_year = period_end.year

            for year in range(start_year, end_year + 1):
                # Calculate days in this year
                year_start = date(year, 1, 1)
                year_end = date(year, 12, 31)

                actual_start = max(period_start, year_start)
                actual_end = min(period_end, year_end)

                days = (actual_end - actual_start).days + 1

                result.append({
                    'product_id': product_id,
                    'product_name': product_names[product_id],
                    'report_year': str(year),
                    'total_amount': days * daily_sales
                })

        # Sort by product_id, report_year
        result.sort(key=lambda x: (x['product_id'], x['report_year']))

        return result


class SolutionAlternative:
    def totalSalesAmountByYear(self, products: List[dict], sales: List[dict]) -> List[dict]:
        """Day by day calculation (less efficient but clearer)"""
        product_names = {p['product_id']: p['product_name'] for p in products}

        # Aggregate by (product_id, year)
        yearly_sales = defaultdict(int)

        for sale in sales:
            product_id = sale['product_id']
            period_start = sale['period_start']
            period_end = sale['period_end']
            daily_sales = sale['average_daily_sales']

            # Iterate through each day
            current = period_start
            while current <= period_end:
                yearly_sales[(product_id, current.year)] += daily_sales
                current += timedelta(days=1)

        # Build result
        result = []
        for (product_id, year), amount in yearly_sales.items():
            result.append({
                'product_id': product_id,
                'product_name': product_names[product_id],
                'report_year': str(year),
                'total_amount': amount
            })

        result.sort(key=lambda x: (x['product_id'], x['report_year']))
        return result
