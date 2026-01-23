#1978. Employees Whose Manager Left the Company
#Easy
#
#Table: Employees
#+-------------+----------+
#| Column Name | Type     |
#+-------------+----------+
#| employee_id | int      |
#| name        | varchar  |
#| manager_id  | int      |
#| salary      | int      |
#+-------------+----------+
#employee_id is the primary key for this table.
#This table contains information about the employees, their salary, and the ID
#of their manager. Some employees do not have a manager (manager_id is null).
#
#Write an SQL query to report the IDs of the employees whose salary is strictly
#less than $30000 and whose manager left the company. When a manager leaves the
#company, their information is deleted from the Employees table, but the reports
#still have their manager_id set to the manager that left.
#
#Return the result table ordered by employee_id.
#
#This is a SQL problem. Below is a Python simulation approach.

from typing import List

class Solution:
    def employeesWithManagerLeft(self, employees: List[dict]) -> List[int]:
        """
        Find employees with salary < 30000 whose manager is not in the company.
        """
        # Get all employee IDs
        all_ids = {emp['employee_id'] for emp in employees}

        result = []

        for emp in employees:
            # Check salary condition
            if emp['salary'] >= 30000:
                continue

            # Check if has manager who left
            manager_id = emp.get('manager_id')
            if manager_id is not None and manager_id not in all_ids:
                result.append(emp['employee_id'])

        return sorted(result)


class SolutionExplicit:
    def employeesWithManagerLeft(self, employees: List[dict]) -> List[int]:
        """
        More explicit version.
        """
        employee_ids = set()
        candidates = []

        # First pass: collect all employee IDs
        for emp in employees:
            employee_ids.add(emp['employee_id'])

        # Second pass: find qualifying employees
        for emp in employees:
            if emp['salary'] < 30000:
                manager_id = emp.get('manager_id')
                # Manager exists but left the company
                if manager_id is not None and manager_id not in employee_ids:
                    candidates.append(emp['employee_id'])

        return sorted(candidates)


# SQL Solution:
"""
SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id IS NOT NULL
  AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
"""

# Alternative SQL with LEFT JOIN:
"""
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;
"""
