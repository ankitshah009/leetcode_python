#1418. Display Table of Food Orders in a Restaurant
#Medium
#
#Given the array orders, which represents the orders that customers have done
#in a restaurant. More specifically
#orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the
#name of the customer, tableNumberi is the table customer sit at, and foodItemi
#is the item customer orders.
#
#Return the restaurant's "display table". The "display table" is a table whose
#row entries denote how many of each food item each table ordered. The first
#column is the table number and the remaining columns correspond to each food
#item in alphabetical order. The first row should be a header whose first column
#is "Table", followed by the names of the food items. Note that the customer
#names are not part of the table. Additionally, the rows should be sorted in
#numerically increasing order.
#
#Example 1:
#Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],
#["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],
#["Gy","1","Water"]]
#Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
#["1","0","0","0","1"],["3","0","1","1","0"],["5","0","1","0","1"],
#["10","1","0","0","0"]]
#Explanation:
#The displaying table looks like:
#Table,Beef Burrito,Ceviche,Fried Chicken,Water
#1    ,0           ,0      ,0            ,1
#3    ,0           ,1      ,1            ,0
#5    ,0           ,1      ,0            ,1
#10   ,1           ,0      ,0            ,0
#
#Constraints:
#    1 <= orders.length <= 5 * 10^4
#    orders[i].length == 3
#    1 <= customerNamei.length, foodItemi.length <= 20
#    customerNamei and foodItemi consist of lowercase and uppercase English
#    letters and the space character.
#    tableNumberi is a valid integer between 1 and 500.

from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """
        Build a mapping of (table, food) -> count.
        """
        # Count orders per (table, food)
        table_orders = defaultdict(lambda: defaultdict(int))
        all_foods = set()
        all_tables = set()

        for customer, table, food in orders:
            table_num = int(table)
            table_orders[table_num][food] += 1
            all_foods.add(food)
            all_tables.add(table_num)

        # Sort foods alphabetically and tables numerically
        sorted_foods = sorted(all_foods)
        sorted_tables = sorted(all_tables)

        # Build result
        result = []

        # Header row
        header = ["Table"] + sorted_foods
        result.append(header)

        # Data rows
        for table in sorted_tables:
            row = [str(table)]
            for food in sorted_foods:
                row.append(str(table_orders[table][food]))
            result.append(row)

        return result


class SolutionCounter:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """Using Counter"""
        from collections import Counter

        foods = set()
        tables = set()
        counts = Counter()

        for _, table, food in orders:
            t = int(table)
            tables.add(t)
            foods.add(food)
            counts[(t, food)] += 1

        sorted_foods = sorted(foods)
        sorted_tables = sorted(tables)

        result = [["Table"] + sorted_foods]

        for t in sorted_tables:
            row = [str(t)]
            for f in sorted_foods:
                row.append(str(counts[(t, f)]))
            result.append(row)

        return result


class SolutionExplicit:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """More explicit step-by-step"""
        # Step 1: Collect all unique foods and tables
        foods = set()
        tables = set()

        for order in orders:
            tables.add(int(order[1]))
            foods.add(order[2])

        # Step 2: Sort them
        sorted_foods = sorted(foods)
        sorted_tables = sorted(tables)

        # Step 3: Create food index mapping
        food_idx = {food: i for i, food in enumerate(sorted_foods)}

        # Step 4: Count orders per table
        table_counts = {t: [0] * len(sorted_foods) for t in sorted_tables}

        for order in orders:
            table = int(order[1])
            food = order[2]
            table_counts[table][food_idx[food]] += 1

        # Step 5: Build result
        result = [["Table"] + sorted_foods]

        for table in sorted_tables:
            row = [str(table)] + [str(c) for c in table_counts[table]]
            result.append(row)

        return result
