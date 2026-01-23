#586. Customer Placing the Largest Number of Orders
#Easy
#
#Table: Orders
#+-----------------+----------+
#| Column Name     | Type     |
#+-----------------+----------+
#| order_number    | int      |
#| customer_number | int      |
#+-----------------+----------+
#order_number is the primary key for this table.
#
#Write a solution to find the customer_number for the customer who has placed the
#largest number of orders.
#
#The test cases are generated so that exactly one customer will have placed more
#orders than any other customer.

# SQL Solution:
# SELECT customer_number
# FROM Orders
# GROUP BY customer_number
# ORDER BY COUNT(*) DESC
# LIMIT 1;

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Pandas solution"""
    # Count orders per customer
    counts = orders.groupby('customer_number').size().reset_index(name='order_count')

    # Get customer with max orders
    max_customer = counts.loc[counts['order_count'].idxmax(), 'customer_number']

    return pd.DataFrame({'customer_number': [max_customer]})


def largest_orders_alt(orders: pd.DataFrame) -> pd.DataFrame:
    """Alternative using value_counts"""
    counts = orders['customer_number'].value_counts()
    return pd.DataFrame({'customer_number': [counts.idxmax()]})
