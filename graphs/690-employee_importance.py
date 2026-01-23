#690. Employee Importance
#Medium
#
#You have a data structure of employee information, including the employee's
#unique ID, importance value, and direct subordinates' IDs.
#
#You are given an array of employees where:
#- employees[i].id is the ID of the ith employee.
#- employees[i].importance is the importance value of the ith employee.
#- employees[i].subordinates is a list of the IDs of the direct subordinates
#  of the ith employee.
#
#Given an integer id that represents an employee's ID, return the total
#importance value of this employee and all their direct and indirect
#subordinates.
#
#Example 1:
#Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
#Output: 11
#Explanation: Employee 1 has importance value 5 and has two direct subordinates:
#employee 2 and employee 3. They both have importance value 3.
#Total = 5 + 3 + 3 = 11.
#
#Example 2:
#Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
#Output: -3
#
#Constraints:
#    1 <= employees.length <= 2000
#    1 <= employees[i].id <= 2000
#    All employees[i].id are unique.
#    -100 <= employees[i].importance <= 100
#    One employee has at most one direct leader and may have several subordinates.
#    The employees have no circular references.

# Definition for Employee.
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: list[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id: int) -> int:
        """
        DFS: Sum importance of employee and all subordinates recursively.
        """
        emp_map = {e.id: e for e in employees}

        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)


class SolutionBFS:
    """BFS approach using queue"""

    def getImportance(self, employees, id: int) -> int:
        from collections import deque

        emp_map = {e.id: e for e in employees}

        total = 0
        queue = deque([id])

        while queue:
            emp_id = queue.popleft()
            emp = emp_map[emp_id]
            total += emp.importance
            queue.extend(emp.subordinates)

        return total


class SolutionIterative:
    """Iterative DFS using stack"""

    def getImportance(self, employees, id: int) -> int:
        emp_map = {e.id: e for e in employees}

        total = 0
        stack = [id]

        while stack:
            emp_id = stack.pop()
            emp = emp_map[emp_id]
            total += emp.importance
            stack.extend(emp.subordinates)

        return total
