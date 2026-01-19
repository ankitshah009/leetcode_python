#184. Department Highest Salary
#Medium
#
#SQL Schema:
#Table: Employee
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#| salary      | int     |
#| departmentId| int     |
#+-------------+---------+
#id is the primary key for this table.
#
#Table: Department
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#+-------------+---------+
#id is the primary key for this table.
#
#Write a solution to find employees who have the highest salary in each
#department.
#
#Example:
#Input:
#Employee table:
#+----+-------+--------+--------------+
#| id | name  | salary | departmentId |
#+----+-------+--------+--------------+
#| 1  | Joe   | 70000  | 1            |
#| 2  | Jim   | 90000  | 1            |
#| 3  | Henry | 80000  | 2            |
#| 4  | Sam   | 60000  | 2            |
#| 5  | Max   | 90000  | 1            |
#+----+-------+--------+--------------+
#Department table:
#+----+-------+
#| id | name  |
#+----+-------+
#| 1  | IT    |
#| 2  | Sales |
#+----+-------+
#Output:
#+------------+----------+--------+
#| Department | Employee | Salary |
#+------------+----------+--------+
#| IT         | Jim      | 90000  |
#| IT         | Max      | 90000  |
#| Sales      | Henry    | 80000  |
#+------------+----------+--------+

# SQL Solution:
"""
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
"""

# SQL Solution using window function:
"""
SELECT Department, Employee, Salary
FROM (
    SELECT d.name AS Department,
           e.name AS Employee,
           e.salary AS Salary,
           RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) as rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) ranked
WHERE rnk = 1;
"""

# Pandas Solution:
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Find max salary per department
    max_salaries = employee.groupby('departmentId')['salary'].transform('max')

    # Filter employees with max salary
    top_earners = employee[employee['salary'] == max_salaries]

    # Merge with department names
    result = top_earners.merge(department, left_on='departmentId', right_on='id')

    return result[['name_y', 'name_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}
    )
