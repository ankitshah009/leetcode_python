#577. Employee Bonus
#Easy
#
#Table: Employee
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| empId       | int     |
#| name        | varchar |
#| supervisor  | int     |
#| salary      | int     |
#+-------------+---------+
#empId is the column with unique values for this table.
#
#Table: Bonus
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| empId       | int  |
#| bonus       | int  |
#+-------------+------+
#empId is the column of unique values for this table.
#
#Write a solution to report the name and bonus amount of each employee with a
#bonus less than 1000.
#
#Return the result table in any order.

# SQL Solution:
# SELECT e.name, b.bonus
# FROM Employee e
# LEFT JOIN Bonus b ON e.empId = b.empId
# WHERE b.bonus < 1000 OR b.bonus IS NULL;

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """Pandas solution"""
    # Left join employee with bonus
    merged = employee.merge(bonus, on='empId', how='left')

    # Filter for bonus < 1000 or NULL
    result = merged[(merged['bonus'] < 1000) | (merged['bonus'].isna())]

    return result[['name', 'bonus']]


def employee_bonus_alt(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """Alternative approach"""
    merged = pd.merge(employee, bonus, on='empId', how='left')
    filtered = merged.query('bonus < 1000 or bonus != bonus')  # NaN != NaN
    return filtered[['name', 'bonus']]
