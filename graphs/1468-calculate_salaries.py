#1468. Calculate Salaries
#Medium (SQL)
#
#Table: Salaries
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| company_id    | int     |
#| employee_id   | int     |
#| employee_name | varchar |
#| salary        | int     |
#+---------------+---------+
#(company_id, employee_id) is the primary key for this table.
#This table contains the company id, the id, the name, and the salary for an
#employee.
#
#Write an SQL query to find the salaries of the employees after applying taxes.
#Round the salary to the nearest integer.
#
#The tax rate is calculated for each company based on the following criteria:
#    0% If the max salary of any employee in the company is less than $1000.
#    24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
#    49% If the max salary of any employee in the company is greater than $10000.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Salaries table:
#+------------+-------------+---------------+--------+
#| company_id | employee_id | employee_name | salary |
#+------------+-------------+---------------+--------+
#| 1          | 1           | Tony          | 2000   |
#| 1          | 2           | Pronub        | 21300  |
#| 1          | 3           | Tyber         | 10800  |
#| 2          | 1           | Pam           | 300    |
#| 2          | 7           | Bassem        | 450    |
#| 2          | 9           | Hermione      | 700    |
#| 3          | 7           | Bocez         | 100    |
#| 3          | 2           | Ognjen        | 2200   |
#| 3          | 13          | Nyan Cat      | 3300   |
#| 3          | 15          | Moreli        | 2100   |
#+------------+-------------+---------------+--------+
#Output:
#+------------+-------------+---------------+--------+
#| company_id | employee_id | employee_name | salary |
#+------------+-------------+---------------+--------+
#| 1          | 1           | Tony          | 1020   |
#| 1          | 2           | Pronub        | 10863  |
#| 1          | 3           | Tyber         | 5765   |
#| 2          | 1           | Pam           | 300    |
#| 2          | 7           | Bassem        | 450    |
#| 2          | 9           | Hermione      | 700    |
#| 3          | 7           | Bocez         | 76     |
#| 3          | 2           | Ognjen        | 1672   |
#| 3          | 13          | Nyan Cat      | 2508   |
#| 3          | 15          | Moreli        | 1596   |
#+------------+-------------+---------------+--------+

#SQL Solution:
#SELECT
#    s.company_id,
#    s.employee_id,
#    s.employee_name,
#    ROUND(s.salary * (1 - CASE
#        WHEN m.max_salary < 1000 THEN 0
#        WHEN m.max_salary <= 10000 THEN 0.24
#        ELSE 0.49
#    END)) AS salary
#FROM Salaries s
#JOIN (
#    SELECT company_id, MAX(salary) AS max_salary
#    FROM Salaries
#    GROUP BY company_id
#) m ON s.company_id = m.company_id;

from typing import List
from collections import defaultdict

class Solution:
    def calculateSalaries(self, salaries: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        1. Find max salary per company
        2. Determine tax rate
        3. Apply tax and round
        """
        # Find max salary per company
        max_salary = defaultdict(int)
        for emp in salaries:
            company = emp['company_id']
            max_salary[company] = max(max_salary[company], emp['salary'])

        # Calculate tax rate per company
        def get_tax_rate(max_sal: int) -> float:
            if max_sal < 1000:
                return 0.0
            elif max_sal <= 10000:
                return 0.24
            else:
                return 0.49

        # Apply taxes
        result = []
        for emp in salaries:
            company = emp['company_id']
            tax_rate = get_tax_rate(max_salary[company])
            new_salary = round(emp['salary'] * (1 - tax_rate))

            result.append({
                'company_id': emp['company_id'],
                'employee_id': emp['employee_id'],
                'employee_name': emp['employee_name'],
                'salary': new_salary
            })

        return result


class SolutionExplicit:
    def calculateSalaries(self, salaries: List[dict]) -> List[dict]:
        """More explicit step-by-step solution"""
        # Step 1: Group by company and find max salary
        companies = defaultdict(list)
        for emp in salaries:
            companies[emp['company_id']].append(emp)

        max_salaries = {}
        for company_id, employees in companies.items():
            max_salaries[company_id] = max(e['salary'] for e in employees)

        # Step 2: Determine tax rates
        tax_rates = {}
        for company_id, max_sal in max_salaries.items():
            if max_sal < 1000:
                tax_rates[company_id] = 0.0
            elif max_sal <= 10000:
                tax_rates[company_id] = 0.24
            else:
                tax_rates[company_id] = 0.49

        # Step 3: Apply taxes
        result = []
        for emp in salaries:
            company = emp['company_id']
            after_tax = round(emp['salary'] * (1 - tax_rates[company]))

            result.append({
                'company_id': company,
                'employee_id': emp['employee_id'],
                'employee_name': emp['employee_name'],
                'salary': after_tax
            })

        return result
