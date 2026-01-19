#183. Customers Who Never Order
#Easy
#
#SQL Schema:
#Table: Customers
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#+-------------+---------+
#id is the primary key for this table.
#
#Table: Orders
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| id          | int  |
#| customerId  | int  |
#+-------------+------+
#id is the primary key for this table.
#customerId references Customers(id).
#
#Write a solution to find all customers who never order anything.
#
#Example:
#Input:
#Customers table:
#+----+-------+
#| id | name  |
#+----+-------+
#| 1  | Joe   |
#| 2  | Henry |
#| 3  | Sam   |
#| 4  | Max   |
#+----+-------+
#Orders table:
#+----+------------+
#| id | customerId |
#+----+------------+
#| 1  | 3          |
#| 2  | 1          |
#+----+------------+
#Output:
#+-----------+
#| Customers |
#+-----------+
#| Henry     |
#| Max       |
#+-----------+

# SQL Solution using NOT IN:
"""
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);
"""

# SQL Solution using LEFT JOIN:
"""
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.id IS NULL;
"""

# SQL Solution using NOT EXISTS:
"""
SELECT c.name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1 FROM Orders o WHERE o.customerId = c.id
);
"""

# Pandas Solution:
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Find customer IDs that have orders
    customers_with_orders = set(orders['customerId'])

    # Filter customers without orders
    result = customers[~customers['id'].isin(customers_with_orders)]

    return pd.DataFrame({'Customers': result['name']})


def find_customers_merge(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Using left merge"""
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    no_orders = merged[merged['customerId'].isna()]
    return pd.DataFrame({'Customers': no_orders['name']})
