#181. Employees Earning More Than Their Managers
#Easy
#
#SQL Schema:
#Table: Employee
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#| salary      | int     |
#| managerId   | int     |
#+-------------+---------+
#id is the primary key for this table.
#Each row indicates the ID, name, salary, and manager of an employee.
#
#Write a solution to find employees who earn more than their managers.
#
#Example:
#Input:
#Employee table:
#+----+-------+--------+-----------+
#| id | name  | salary | managerId |
#+----+-------+--------+-----------+
#| 1  | Joe   | 70000  | 3         |
#| 2  | Henry | 80000  | 4         |
#| 3  | Sam   | 60000  | Null      |
#| 4  | Max   | 90000  | Null      |
#+----+-------+--------+-----------+
#Output:
#+----------+
#| Employee |
#+----------+
#| Joe      |
#+----------+
#Explanation: Joe is the only employee who earns more than his manager.

# SQL Solution using JOIN:
"""
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
"""

# SQL Solution using subquery:
"""
SELECT e.name AS Employee
FROM Employee e
WHERE e.salary > (
    SELECT m.salary
    FROM Employee m
    WHERE m.id = e.managerId
);
"""

# Pandas Solution:
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Self-merge to get manager info
    merged = employee.merge(
        employee[['id', 'salary']],
        left_on='managerId',
        right_on='id',
        suffixes=('', '_manager')
    )

    # Filter employees earning more than managers
    result = merged[merged['salary'] > merged['salary_manager']]

    return pd.DataFrame({'Employee': result['name']})


def find_employees_alternative(employee: pd.DataFrame) -> pd.DataFrame:
    """Using map for manager salary lookup"""
    manager_salary = employee.set_index('id')['salary'].to_dict()

    employee['manager_salary'] = employee['managerId'].map(manager_salary)

    result = employee[employee['salary'] > employee['manager_salary']]['name']

    return pd.DataFrame({'Employee': result})
