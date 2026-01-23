#1045. Customers Who Bought All Products
#Medium
#
#Table: Customer
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| customer_id | int     |
#| product_key | int     |
#+-------------+---------+
#This table may contain duplicates. customer_id is not NULL.
#product_key is a foreign key (reference column) to Product table.
#
#Table: Product
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| product_key | int     |
#+-------------+---------+
#product_key is the primary key (column with unique values) for this table.
#
#Write a solution to report the customer ids from the Customer table that
#bought all the products in the Product table.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Customer table:
#+-------------+-------------+
#| customer_id | product_key |
#+-------------+-------------+
#| 1           | 5           |
#| 2           | 6           |
#| 3           | 5           |
#| 3           | 6           |
#| 1           | 6           |
#+-------------+-------------+
#Product table:
#+-------------+
#| product_key |
#+-------------+
#| 5           |
#| 6           |
#+-------------+
#Output:
#+-------------+
#| customer_id |
#+-------------+
#| 1           |
#| 3           |
#+-------------+
#Explanation:
#Customers 1 and 3 bought both products 5 and 6.
#Customer 2 only bought product 6.

# SQL Solution:
#
# SELECT customer_id
# FROM Customer
# GROUP BY customer_id
# HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)

# Python/Pandas Solution:
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Find customers who bought all products.
    """
    total_products = product['product_key'].nunique()

    customer_products = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    customer_products.columns = ['customer_id', 'product_count']

    result = customer_products[customer_products['product_count'] == total_products][['customer_id']]

    return result


def find_customers_alternative(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """Alternative using set operations"""
    all_products = set(product['product_key'])

    def bought_all(group):
        return set(group['product_key']) >= all_products

    result = customer.groupby('customer_id').filter(
        lambda x: set(x['product_key']) >= all_products
    )['customer_id'].drop_duplicates().to_frame()

    return result
