#584. Find Customer Referee
#Easy
#
#Table: Customer
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#| referee_id  | int     |
#+-------------+---------+
#In SQL, id is the primary key column for this table.
#
#Find the names of the customer that are not referred by the customer with id = 2.
#
#Return the result table in any order.

# SQL Solution:
# SELECT name
# FROM Customer
# WHERE referee_id != 2 OR referee_id IS NULL;

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    """Pandas solution"""
    # Filter customers not referred by id 2 (including NULL)
    result = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
    return result[['name']]


def find_customer_referee_alt(customer: pd.DataFrame) -> pd.DataFrame:
    """Alternative using fillna"""
    customer['referee_id'] = customer['referee_id'].fillna(0)
    result = customer[customer['referee_id'] != 2]
    return result[['name']]
