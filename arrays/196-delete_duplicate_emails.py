#196. Delete Duplicate Emails
#Easy
#
#SQL Schema:
#Table: Person
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| email       | varchar |
#+-------------+---------+
#id is the primary key column for this table.
#
#Write a solution to delete all duplicate emails, keeping only one unique email
#with the smallest id.
#
#Example:
#Input:
#Person table:
#+----+------------------+
#| id | email            |
#+----+------------------+
#| 1  | john@example.com |
#| 2  | bob@example.com  |
#| 3  | john@example.com |
#+----+------------------+
#Output:
#+----+------------------+
#| id | email            |
#+----+------------------+
#| 1  | john@example.com |
#| 2  | bob@example.com  |
#+----+------------------+
#Explanation: john@example.com is repeated two times. We keep the row with
#smallest id = 1.

# SQL Solution 1: Using self-join DELETE
"""
DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;
"""

# SQL Solution 2: Using NOT IN with subquery
"""
DELETE FROM Person
WHERE id NOT IN (
    SELECT * FROM (
        SELECT MIN(id)
        FROM Person
        GROUP BY email
    ) AS temp
);
"""

# SQL Solution 3: Using ROW_NUMBER (for databases that support it)
"""
DELETE FROM Person
WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as rn
        FROM Person
    ) ranked
    WHERE rn > 1
);
"""

# Pandas Solution (for modification in place):
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    Modify Person in place to delete duplicate emails.
    Keep the row with smallest id.
    """
    # Sort by id to ensure we keep the smallest id
    person.sort_values('id', inplace=True)

    # Drop duplicates keeping first (smallest id due to sort)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


def delete_duplicate_emails_mask(person: pd.DataFrame) -> None:
    """Alternative using boolean mask"""
    # Find the minimum id for each email
    min_ids = person.groupby('email')['id'].transform('min')

    # Keep only rows where id equals the minimum id for that email
    mask = person['id'] == min_ids
    person.drop(person[~mask].index, inplace=True)
