#1543. Fix Product Name Format
#Easy (SQL)
#
#Table: Sales
#+--------------+---------+
#| Column Name  | Type    |
#+--------------+---------+
#| sale_id      | int     |
#| product_name | varchar |
#| sale_date    | date    |
#+--------------+---------+
#sale_id is the primary key for this table.
#Each row of this table contains the product name and the date it was sold.
#
#Since table Sales was filled manually in the year 2000, product_name may contain
#leading and/or trailing white spaces, also they are case-insensitive.
#
#Write an SQL query to report
#- product_name in lowercase without leading or trailing white spaces.
#- sale_date in the format ('YYYY-MM').
#- total the number of times the product was sold in this month.
#
#Return the result table ordered by product_name in ascending order. In case of
#a tie, order it by sale_date in ascending order.
#
#Example 1:
#Input:
#Sales table:
#+---------+--------------+------------+
#| sale_id | product_name | sale_date  |
#+---------+--------------+------------+
#| 1       | LCPHONE      | 2000-01-16 |
#| 2       | LCPhone      | 2000-01-17 |
#| 3       | LcPhOnE      | 2000-02-18 |
#| 4       | LCKeyCHAiN   | 2000-02-19 |
#| 5       | LCKeyworD    | 2000-02-28 |
#| 6       | lcphone      | 2000-02-21 |
#| 7       |  LcPhOnE     | 2000-02-21 |
#| 8       |  LCKeyCHAiN  | 2000-02-21 |
#+---------+--------------+------------+
#
#Output:
#+--------------+-----------+-------+
#| product_name | sale_date | total |
#+--------------+-----------+-------+
#| lckeychain   | 2000-02   | 2     |
#| lckeyword    | 2000-02   | 1     |
#| lcphone      | 2000-01   | 2     |
#| lcphone      | 2000-02   | 2     |
#+--------------+-----------+-------+

#SQL Solution:
#SELECT
#    LOWER(TRIM(product_name)) AS product_name,
#    DATE_FORMAT(sale_date, '%Y-%m') AS sale_date,
#    COUNT(*) AS total
#FROM Sales
#GROUP BY LOWER(TRIM(product_name)), DATE_FORMAT(sale_date, '%Y-%m')
#ORDER BY product_name, sale_date;

from typing import List
from collections import defaultdict

class Solution:
    def fixProductNameFormat(self, sales: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Normalize product names and group by month.
        """
        # Group by (normalized_name, year-month)
        counts = defaultdict(int)

        for sale in sales:
            name = sale['product_name'].strip().lower()
            date = sale['sale_date']

            # Extract year-month
            if isinstance(date, str):
                year_month = date[:7]
            else:
                year_month = date.strftime('%Y-%m')

            counts[(name, year_month)] += 1

        # Build result
        result = []
        for (name, year_month), total in counts.items():
            result.append({
                'product_name': name,
                'sale_date': year_month,
                'total': total
            })

        # Sort by product_name, then sale_date
        result.sort(key=lambda x: (x['product_name'], x['sale_date']))

        return result


class SolutionGroupBy:
    def fixProductNameFormat(self, sales: List[dict]) -> List[dict]:
        """
        Using itertools.groupby after sorting.
        """
        from itertools import groupby

        # Normalize and extract month
        processed = []
        for sale in sales:
            name = sale['product_name'].strip().lower()
            date = sale['sale_date']
            if isinstance(date, str):
                month = date[:7]
            else:
                month = date.strftime('%Y-%m')
            processed.append((name, month))

        # Sort for groupby
        processed.sort()

        # Group and count
        result = []
        for key, group in groupby(processed):
            name, month = key
            count = sum(1 for _ in group)
            result.append({
                'product_name': name,
                'sale_date': month,
                'total': count
            })

        return result


class SolutionCounter:
    def fixProductNameFormat(self, sales: List[dict]) -> List[dict]:
        """
        Using Counter for counting.
        """
        from collections import Counter

        keys = []
        for sale in sales:
            name = sale['product_name'].strip().lower()
            date = sale['sale_date']
            month = date[:7] if isinstance(date, str) else date.strftime('%Y-%m')
            keys.append((name, month))

        counts = Counter(keys)

        result = [
            {'product_name': name, 'sale_date': month, 'total': total}
            for (name, month), total in counts.items()
        ]

        result.sort(key=lambda x: (x['product_name'], x['sale_date']))
        return result


class SolutionPandas:
    def fixProductNameFormat(self, sales: List[dict]) -> List[dict]:
        """
        Using pandas (if available) for cleaner data manipulation.
        """
        try:
            import pandas as pd

            df = pd.DataFrame(sales)

            # Normalize
            df['product_name'] = df['product_name'].str.strip().str.lower()
            df['sale_date'] = pd.to_datetime(df['sale_date']).dt.strftime('%Y-%m')

            # Group and count
            result = df.groupby(['product_name', 'sale_date']).size().reset_index(name='total')
            result = result.sort_values(['product_name', 'sale_date'])

            return result.to_dict('records')
        except ImportError:
            # Fall back to non-pandas solution
            return SolutionCounter().fixProductNameFormat(sales)
