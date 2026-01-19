#176. Second Highest Salary
#Medium
#
#SQL Schema:
#Table: Employee
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| id          | int  |
#| salary      | int  |
#+-------------+------+
#id is the primary key column for this table.
#
#Write a solution to find the second highest salary from the Employee table.
#If there is no second highest salary, return null.
#
#Example 1:
#Input:
#Employee table:
#+----+--------+
#| id | salary |
#+----+--------+
#| 1  | 100    |
#| 2  | 200    |
#| 3  | 300    |
#+----+--------+
#Output:
#+---------------------+
#| SecondHighestSalary |
#+---------------------+
#| 200                 |
#+---------------------+
#
#Example 2:
#Input:
#Employee table:
#+----+--------+
#| id | salary |
#+----+--------+
#| 1  | 100    |
#+----+--------+
#Output:
#+---------------------+
#| SecondHighestSalary |
#+---------------------+
#| null                |
#+---------------------+

# SQL Solutions:

# Solution 1: Using LIMIT and OFFSET
"""
SELECT
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;
"""

# Solution 2: Using MAX with subquery
"""
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
"""

# Solution 3: Using IFNULL for MySQL
"""
SELECT IFNULL(
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1),
    NULL
) AS SecondHighestSalary;
"""

# Pandas Solution:
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().nlargest(2)

    if len(unique_salaries) < 2:
        result = None
    else:
        result = unique_salaries.iloc[1]

    return pd.DataFrame({'SecondHighestSalary': [result]})


def second_highest_salary_alternative(employee: pd.DataFrame) -> pd.DataFrame:
    """Using sort and indexing"""
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    second_highest = unique_salaries.iloc[1] if len(unique_salaries) >= 2 else None

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})
