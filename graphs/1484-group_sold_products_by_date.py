#1484. Group Sold Products By The Date
#Easy (SQL)
#
#Table Activities:
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| sell_date   | date    |
#| product     | varchar |
#+-------------+---------+
#There is no primary key for this table, it may contain duplicates.
#Each row of this table contains the product name and the date it was sold in
#a market.
#
#Write an SQL query to find for each date the number of different products sold
#and their names.
#
#The sold products names for each date should be sorted lexicographically.
#
#Return the result table ordered by sell_date.
#
#Example 1:
#Input:
#Activities table:
#+------------+------------+
#| sell_date  | product    |
#+------------+------------+
#| 2020-05-30 | Headphone  |
#| 2020-06-01 | Pencil     |
#| 2020-06-02 | Mask       |
#| 2020-05-30 | Basketball |
#| 2020-06-01 | Bible      |
#| 2020-06-02 | Mask       |
#| 2020-05-30 | T-Shirt    |
#+------------+------------+
#Output:
#+------------+----------+------------------------------+
#| sell_date  | num_sold | products                     |
#+------------+----------+------------------------------+
#| 2020-05-30 | 3        | Basketball,Headphone,T-Shirt |
#| 2020-06-01 | 2        | Bible,Pencil                 |
#| 2020-06-02 | 1        | Mask                         |
#+------------+----------+------------------------------+

#SQL Solution:
#SELECT
#    sell_date,
#    COUNT(DISTINCT product) AS num_sold,
#    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
#FROM Activities
#GROUP BY sell_date
#ORDER BY sell_date;

from typing import List
from collections import defaultdict

class Solution:
    def groupSoldProductsByDate(self, activities: List[dict]) -> List[dict]:
        """
        Python simulation of SQL GROUP_CONCAT query.
        """
        # Group products by date
        date_products = defaultdict(set)

        for activity in activities:
            date = activity['sell_date']
            product = activity['product']
            date_products[date].add(product)

        # Build result
        result = []
        for date in sorted(date_products.keys()):
            products = sorted(date_products[date])
            result.append({
                'sell_date': date,
                'num_sold': len(products),
                'products': ','.join(products)
            })

        return result


class SolutionExplicit:
    def groupSoldProductsByDate(self, activities: List[dict]) -> List[dict]:
        """More explicit implementation"""
        # Step 1: Group by date and collect unique products
        groups = {}

        for activity in activities:
            date = activity['sell_date']
            product = activity['product']

            if date not in groups:
                groups[date] = set()
            groups[date].add(product)

        # Step 2: Sort dates
        sorted_dates = sorted(groups.keys())

        # Step 3: Build result with sorted products
        result = []
        for date in sorted_dates:
            products = sorted(groups[date])  # Lexicographically sorted
            result.append({
                'sell_date': date,
                'num_sold': len(products),
                'products': ','.join(products)
            })

        return result


class SolutionPandas:
    def groupSoldProductsByDate(self, activities: List[dict]) -> List[dict]:
        """
        Using pandas-like approach (pseudocode).
        In real pandas:
        df.groupby('sell_date').agg(
            num_sold=('product', 'nunique'),
            products=('product', lambda x: ','.join(sorted(set(x))))
        ).reset_index().sort_values('sell_date')
        """
        from collections import defaultdict

        # Simulate groupby
        grouped = defaultdict(list)
        for act in activities:
            grouped[act['sell_date']].append(act['product'])

        # Aggregate
        result = []
        for date in sorted(grouped.keys()):
            unique_products = sorted(set(grouped[date]))
            result.append({
                'sell_date': date,
                'num_sold': len(unique_products),
                'products': ','.join(unique_products)
            })

        return result
