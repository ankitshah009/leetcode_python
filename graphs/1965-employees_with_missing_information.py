#1965. Employees With Missing Information
#Easy
#
#Table: Employees
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| employee_id | int     |
#| name        | varchar |
#+-------------+---------+
#employee_id is the primary key for this table.
#
#Table: Salaries
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| employee_id | int     |
#| salary      | int     |
#+-------------+---------+
#employee_id is the primary key for this table.
#
#Write an SQL query to report the IDs of all the employees with missing
#information. The information of an employee is missing if:
#- The employee's name is missing, or
#- The employee's salary is missing.
#
#Return the result table ordered by employee_id in ascending order.
#
#This is a SQL problem. Below is a Python simulation approach.

from typing import List

class Solution:
    def employeesWithMissingInfo(self, employees: List[List], salaries: List[List]) -> List[int]:
        """
        Find employees with either missing name or missing salary.
        """
        # Get sets of employee IDs from each table
        emp_ids = {emp[0] for emp in employees}
        sal_ids = {sal[0] for sal in salaries}

        # Find symmetric difference (IDs in one but not both)
        missing = emp_ids.symmetric_difference(sal_ids)

        return sorted(missing)


class SolutionExplicit:
    def employeesWithMissingInfo(self, employees: List[List], salaries: List[List]) -> List[int]:
        """
        Explicit approach showing missing from each table.
        """
        emp_ids = set(emp[0] for emp in employees)
        sal_ids = set(sal[0] for sal in salaries)

        # Missing salary (in employees but not in salaries)
        missing_salary = emp_ids - sal_ids

        # Missing name (in salaries but not in employees)
        missing_name = sal_ids - emp_ids

        # Combine and sort
        return sorted(missing_salary | missing_name)


# SQL Solution:
"""
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)

UNION

SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)

ORDER BY employee_id;
"""

# Alternative SQL with FULL OUTER JOIN:
"""
SELECT COALESCE(e.employee_id, s.employee_id) AS employee_id
FROM Employees e
FULL OUTER JOIN Salaries s ON e.employee_id = s.employee_id
WHERE e.employee_id IS NULL OR s.employee_id IS NULL
ORDER BY employee_id;
"""
