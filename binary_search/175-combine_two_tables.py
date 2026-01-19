#175. Combine Two Tables
#Easy
#
#SQL Schema:
#Table: Person
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| personId    | int     |
#| lastName    | varchar |
#| firstName   | varchar |
#+-------------+---------+
#personId is the primary key column for this table.
#
#Table: Address
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| addressId   | int     |
#| personId    | int     |
#| city        | varchar |
#| state       | varchar |
#+-------------+---------+
#addressId is the primary key column for this table.
#
#Write a solution to report the first name, last name, city, and state of each
#person in the Person table. If the address of a personId is not present in the
#Address table, report null instead.
#
#Example:
#Input:
#Person table:
#+----------+----------+-----------+
#| personId | lastName | firstName |
#+----------+----------+-----------+
#| 1        | Wang     | Allen     |
#| 2        | Alice    | Bob       |
#+----------+----------+-----------+
#Address table:
#+-----------+----------+---------------+------------+
#| addressId | personId | city          | state      |
#+-----------+----------+---------------+------------+
#| 1         | 2        | New York City | New York   |
#| 2         | 3        | Leetcode      | California |
#+-----------+----------+---------------+------------+
#
#Output:
#+-----------+----------+---------------+----------+
#| firstName | lastName | city          | state    |
#+-----------+----------+---------------+----------+
#| Allen     | Wang     | Null          | Null     |
#| Bob       | Alice    | New York City | New York |
#+-----------+----------+---------------+----------+

# SQL Solution:
"""
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
"""

# Pandas Solution:
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address, on='personId', how='left')
    return result[['firstName', 'lastName', 'city', 'state']]


def combine_two_tables_alternative(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """Using join instead of merge"""
    person_indexed = person.set_index('personId')
    address_indexed = address.set_index('personId')

    result = person_indexed.join(address_indexed, how='left')
    return result[['firstName', 'lastName', 'city', 'state']].reset_index(drop=True)
