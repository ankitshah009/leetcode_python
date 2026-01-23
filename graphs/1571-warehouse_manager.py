#1571. Warehouse Manager
#Easy (SQL)
#
#Table: Warehouse
#+--------------+---------+
#| Column Name  | Type    |
#+--------------+---------+
#| name         | varchar |
#| product_id   | int     |
#| units        | int     |
#+--------------+---------+
#(name, product_id) is the primary key for this table.
#Each row of this table contains the information of the products in each warehouse.
#
#Table: Products
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| product_name  | varchar |
#| Width         | int     |
#| Length        | int     |
#| Height        | int     |
#+---------------+---------+
#product_id is the primary key for this table.
#Each row of this table contains the information about the product dimensions.
#
#Write an SQL query to report the number of cubic feet of volume the inventory
#occupies in each warehouse.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Warehouse table:
#+------------+-------------+--------+
#| name       | product_id  | units  |
#+------------+-------------+--------+
#| LCHouse1   | 1           | 1      |
#| LCHouse1   | 2           | 10     |
#| LCHouse1   | 3           | 5      |
#| LCHouse2   | 1           | 2      |
#| LCHouse2   | 2           | 2      |
#| LCHouse3   | 4           | 1      |
#+------------+-------------+--------+
#
#Products table:
#+------------+--------------+-------+--------+--------+
#| product_id | product_name | Width | Length | Height |
#+------------+--------------+-------+--------+--------+
#| 1          | LC-TV        | 5     | 50     | 40     |
#| 2          | LC-KeyChain  | 5     | 5      | 5      |
#| 3          | LC-Phone     | 2     | 10     | 10     |
#| 4          | LC-T-Shirt   | 4     | 10     | 20     |
#+------------+--------------+-------+--------+--------+
#
#Output:
#+----------------+------------+
#| warehouse_name | volume     |
#+----------------+------------+
#| LCHouse1       | 12250      |
#| LCHouse2       | 20500      |
#| LCHouse3       | 800        |
#+----------------+------------+

#SQL Solution:
#SELECT
#    w.name AS warehouse_name,
#    SUM(w.units * p.Width * p.Length * p.Height) AS volume
#FROM Warehouse w
#JOIN Products p ON w.product_id = p.product_id
#GROUP BY w.name;

from typing import List
from collections import defaultdict

class Solution:
    def warehouseManager(
        self,
        warehouse: List[dict],
        products: List[dict]
    ) -> List[dict]:
        """
        Python simulation: Calculate total volume per warehouse.
        """
        # Build product volume lookup
        product_volume = {}
        for p in products:
            volume = p['Width'] * p['Length'] * p['Height']
            product_volume[p['product_id']] = volume

        # Calculate total volume per warehouse
        warehouse_volume = defaultdict(int)

        for w in warehouse:
            pid = w['product_id']
            units = w['units']
            if pid in product_volume:
                warehouse_volume[w['name']] += units * product_volume[pid]

        # Build result
        return [
            {'warehouse_name': name, 'volume': vol}
            for name, vol in warehouse_volume.items()
        ]


class SolutionDetailed:
    def warehouseManager(
        self,
        warehouse: List[dict],
        products: List[dict]
    ) -> List[dict]:
        """
        Detailed step-by-step calculation.
        """
        # Step 1: Calculate volume for each product
        volumes = {
            p['product_id']: p['Width'] * p['Length'] * p['Height']
            for p in products
        }

        # Step 2: Group warehouse entries by name
        warehouse_products = defaultdict(list)
        for w in warehouse:
            warehouse_products[w['name']].append((w['product_id'], w['units']))

        # Step 3: Calculate total volume for each warehouse
        result = []
        for name, items in warehouse_products.items():
            total_volume = sum(
                units * volumes.get(pid, 0)
                for pid, units in items
            )
            result.append({
                'warehouse_name': name,
                'volume': total_volume
            })

        return result
