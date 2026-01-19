#182. Duplicate Emails
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
#id is the primary key for this table.
#
#Write a solution to report all the duplicate emails.
#Return the result table in any order.
#
#Example:
#Input:
#Person table:
#+----+---------+
#| id | email   |
#+----+---------+
#| 1  | a@b.com |
#| 2  | c@d.com |
#| 3  | a@b.com |
#+----+---------+
#Output:
#+---------+
#| Email   |
#+---------+
#| a@b.com |
#+---------+
#Explanation: a@b.com is repeated two times.

# SQL Solution using GROUP BY and HAVING:
"""
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
"""

# SQL Solution using self-join:
"""
SELECT DISTINCT p1.email AS Email
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id != p2.id;
"""

# SQL Solution using subquery:
"""
SELECT DISTINCT email AS Email
FROM Person
WHERE email IN (
    SELECT email
    FROM Person
    GROUP BY email
    HAVING COUNT(*) > 1
);
"""

# Pandas Solution:
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person.groupby('email').size().reset_index(name='count')
    duplicates = email_counts[email_counts['count'] > 1]['email']
    return pd.DataFrame({'Email': duplicates})


def duplicate_emails_value_counts(person: pd.DataFrame) -> pd.DataFrame:
    """Using value_counts"""
    counts = person['email'].value_counts()
    duplicates = counts[counts > 1].index.tolist()
    return pd.DataFrame({'Email': duplicates})


def duplicate_emails_duplicated(person: pd.DataFrame) -> pd.DataFrame:
    """Using duplicated method"""
    duplicates = person[person['email'].duplicated(keep=False)]['email'].unique()
    return pd.DataFrame({'Email': duplicates})
