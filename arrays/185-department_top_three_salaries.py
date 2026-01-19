#185. Department Top Three Salaries
#Hard
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
#A company's executives are interested in seeing who earns the most money in
#each of the company's departments. A high earner in a department is an employee
#who has a salary in the top three unique salaries for that department.
#
#Write a solution to find the employees who are high earners in each department.
#
#Example:
#Input:
#Employee table:
#+----+-------+--------+--------------+
#| id | name  | salary | departmentId |
#+----+-------+--------+--------------+
#| 1  | Joe   | 85000  | 1            |
#| 2  | Henry | 80000  | 2            |
#| 3  | Sam   | 60000  | 2            |
#| 4  | Max   | 90000  | 1            |
#| 5  | Janet | 69000  | 1            |
#| 6  | Randy | 85000  | 1            |
#| 7  | Will  | 70000  | 1            |
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
#| IT         | Max      | 90000  |
#| IT         | Joe      | 85000  |
#| IT         | Randy    | 85000  |
#| IT         | Will     | 70000  |
#| Sales      | Henry    | 80000  |
#| Sales      | Sam      | 60000  |
#+------------+----------+--------+

# SQL Solution using DENSE_RANK:
"""
SELECT Department, Employee, Salary
FROM (
    SELECT d.name AS Department,
           e.name AS Employee,
           e.salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) as rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) ranked
WHERE rnk <= 3;
"""

# SQL Solution using subquery:
"""
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId AND e2.salary > e.salary
) < 3;
"""

# Pandas Solution:
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee with department
    merged = employee.merge(department, left_on='departmentId', right_on='id')

    # Calculate dense rank within each department
    merged['rank'] = merged.groupby('departmentId')['salary'].rank(
        method='dense', ascending=False
    )

    # Filter top 3
    top_three = merged[merged['rank'] <= 3]

    return top_three[['name_y', 'name_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}
    )


def top_three_salaries_nlargest(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """Using nlargest approach"""
    merged = employee.merge(department, left_on='departmentId', right_on='id')

    def get_top_three(group):
        top_salaries = group['salary'].nlargest(3).unique()[:3]
        return group[group['salary'].isin(top_salaries)]

    result = merged.groupby('departmentId', group_keys=False).apply(get_top_three)

    return result[['name_y', 'name_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}
    )
