#1350. Students With Invalid Departments
#Easy
#
#Table: Departments
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| name          | varchar |
#+---------------+---------+
#id is the primary key of this table.
#
#Table: Students
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| name          | varchar |
#| department_id | int     |
#+---------------+---------+
#id is the primary key of this table.
#
#Write an SQL query to find the id and the name of all students who are enrolled
#in departments that no longer exist.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Departments table:
#+------+--------------------------+
#| id   | name                     |
#+------+--------------------------+
#| 1    | Electrical Engineering   |
#| 7    | Computer Engineering     |
#| 13   | Business Administration  |
#+------+--------------------------+
#Students table:
#+------+----------+---------------+
#| id   | name     | department_id |
#+------+----------+---------------+
#| 23   | Alice    | 1             |
#| 1    | Bob      | 7             |
#| 5    | Jennifer | 13            |
#| 2    | John     | 14            |
#| 4    | Jasmine  | 77            |
#| 3    | Steve    | 74            |
#| 6    | Luis     | 1             |
#| 8    | Jonathan | 7             |
#| 7    | Daiana   | 33            |
#| 11   | Madelynn | 1             |
#+------+----------+---------------+
#Output:
#+------+----------+
#| id   | name     |
#+------+----------+
#| 2    | John     |
#| 7    | Daiana   |
#| 4    | Jasmine  |
#| 3    | Steve    |
#+------+----------+

# SQL Solution using LEFT JOIN:
# SELECT s.id, s.name
# FROM Students s
# LEFT JOIN Departments d ON s.department_id = d.id
# WHERE d.id IS NULL;

# SQL Solution using NOT IN:
# SELECT id, name
# FROM Students
# WHERE department_id NOT IN (SELECT id FROM Departments);

# SQL Solution using NOT EXISTS:
# SELECT s.id, s.name
# FROM Students s
# WHERE NOT EXISTS (
#     SELECT 1 FROM Departments d WHERE d.id = s.department_id
# );

# Python simulation
from typing import List, Tuple

class Solution:
    def studentsWithInvalidDepartments(
        self,
        departments: List[Tuple[int, str]],
        students: List[Tuple[int, str, int]]
    ) -> List[Tuple[int, str]]:
        """
        Find students whose department_id doesn't exist in Departments.
        """
        valid_dept_ids = {dept_id for dept_id, _ in departments}

        result = []
        for student_id, name, dept_id in students:
            if dept_id not in valid_dept_ids:
                result.append((student_id, name))

        return result
