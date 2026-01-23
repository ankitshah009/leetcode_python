#1303. Find the Team Size
#Easy
#
#Table: Employee
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| employee_id   | int     |
#| team_id       | int     |
#+---------------+---------+
#employee_id is the primary key for this table.
#Each row of this table contains the ID of each employee and their respective team.
#
#Write an SQL query to find the team size of each of the employees.
#
#Return result table in any order.
#
#Example 1:
#Input:
#Employee table:
#+-------------+------------+
#| employee_id | team_id    |
#+-------------+------------+
#| 1           | 8          |
#| 2           | 8          |
#| 3           | 8          |
#| 4           | 7          |
#| 5           | 9          |
#| 6           | 9          |
#+-------------+------------+
#Output:
#+-------------+------------+
#| employee_id | team_size  |
#+-------------+------------+
#| 1           | 3          |
#| 2           | 3          |
#| 3           | 3          |
#| 4           | 1          |
#| 5           | 2          |
#| 6           | 2          |
#+-------------+------------+

# SQL Solution using window function:
# SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size
# FROM Employee;

# SQL Solution using subquery:
# SELECT e.employee_id,
#     (SELECT COUNT(*) FROM Employee e2 WHERE e2.team_id = e.team_id) AS team_size
# FROM Employee e;

# SQL Solution using join:
# SELECT e.employee_id, t.team_size
# FROM Employee e
# JOIN (
#     SELECT team_id, COUNT(*) AS team_size
#     FROM Employee
#     GROUP BY team_id
# ) t ON e.team_id = t.team_id;

# Python simulation
from typing import List, Tuple
from collections import Counter

class Solution:
    def findTeamSize(self, employees: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Find team size for each employee.
        """
        # Count team sizes
        team_sizes = Counter(team_id for _, team_id in employees)

        # Map each employee to their team size
        return [(emp_id, team_sizes[team_id]) for emp_id, team_id in employees]
