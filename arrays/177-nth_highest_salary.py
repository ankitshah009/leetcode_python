#177. Nth Highest Salary
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
#Write a solution to find the nth highest salary from the Employee table.
#If there is no nth highest salary, return null.
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
#n = 2
#Output:
#+------------------------+
#| getNthHighestSalary(2) |
#+------------------------+
#| 200                    |
#+------------------------+
#
#Example 2:
#Input:
#Employee table:
#+----+--------+
#| id | salary |
#+----+--------+
#| 1  | 100    |
#+----+--------+
#n = 2
#Output:
#+------------------------+
#| getNthHighestSalary(2) |
#+------------------------+
#| null                   |
#+------------------------+

# SQL Solution (MySQL Function):
"""
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END
"""

# Alternative SQL using DENSE_RANK:
"""
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM (
          SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank_num
          FROM Employee
      ) ranked
      WHERE rank_num = N
  );
END
"""

# Pandas Solution:
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().nlargest(N)

    if len(unique_salaries) < N:
        result = None
    else:
        result = unique_salaries.iloc[N - 1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})


def nth_highest_salary_rank(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Using rank function"""
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    nth_salary = employee[employee['rank'] == N]['salary'].drop_duplicates()

    result = nth_salary.iloc[0] if len(nth_salary) > 0 else None
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})
