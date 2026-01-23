#1527. Patients With a Condition
#Easy (SQL)
#
#Table: Patients
#+--------------+---------+
#| Column Name  | Type    |
#+--------------+---------+
#| patient_id   | int     |
#| patient_name | varchar |
#| conditions   | varchar |
#+--------------+---------+
#patient_id is the primary key for this table.
#'conditions' contains 0 or more code separated by spaces.
#This table contains information of the patients in the hospital.
#
#Write an SQL query to report the patient_id, patient_name and conditions of the
#patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Patients table:
#+------------+--------------+--------------+
#| patient_id | patient_name | conditions   |
#+------------+--------------+--------------+
#| 1          | Daniel       | YFEV COUGH   |
#| 2          | Alice        |              |
#| 3          | Bob          | DIAB100 MYOP |
#| 4          | George       | ACNE DIAB100 |
#| 5          | Alain        | DIAB201      |
#+------------+--------------+--------------+
#Output:
#+------------+--------------+--------------+
#| patient_id | patient_name | conditions   |
#+------------+--------------+--------------+
#| 3          | Bob          | DIAB100 MYOP |
#| 4          | George       | ACNE DIAB100 |
#+------------+--------------+--------------+
#Explanation: Bob and George both have a condition that starts with DIAB1.

#SQL Solution:
#SELECT *
#FROM Patients
#WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
#
#-- Alternative using REGEXP:
#-- SELECT *
#-- FROM Patients
#-- WHERE conditions REGEXP '\\bDIAB1';

from typing import List
import re

class Solution:
    def patientsWithCondition(self, patients: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Find patients with a condition starting with DIAB1.
        """
        result = []

        for patient in patients:
            conditions = patient.get('conditions', '')

            # Check if any condition starts with DIAB1
            # Either at the beginning or after a space
            if conditions.startswith('DIAB1') or ' DIAB1' in conditions:
                result.append(patient)

        return result


class SolutionRegex:
    def patientsWithCondition(self, patients: List[dict]) -> List[dict]:
        """Using regex for word boundary matching"""
        pattern = re.compile(r'\bDIAB1')

        result = []
        for patient in patients:
            conditions = patient.get('conditions', '')
            if pattern.search(conditions):
                result.append(patient)

        return result


class SolutionSplit:
    def patientsWithCondition(self, patients: List[dict]) -> List[dict]:
        """
        Split conditions and check each one.
        """
        result = []

        for patient in patients:
            conditions = patient.get('conditions', '')
            condition_list = conditions.split()

            has_diab1 = any(cond.startswith('DIAB1') for cond in condition_list)

            if has_diab1:
                result.append(patient)

        return result


class SolutionExplicit:
    def patientsWithCondition(self, patients: List[dict]) -> List[dict]:
        """
        Explicit check for DIAB1 prefix.
        """
        def has_type1_diabetes(conditions: str) -> bool:
            if not conditions:
                return False

            # Split by spaces
            codes = conditions.split()

            for code in codes:
                if code.startswith('DIAB1'):
                    return True

            return False

        return [p for p in patients if has_type1_diabetes(p.get('conditions', ''))]
