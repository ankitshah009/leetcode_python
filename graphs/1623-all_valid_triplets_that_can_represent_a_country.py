#1623. All Valid Triplets That Can Represent a Country
#Easy (SQL)
#
#Table: SchoolA
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| student_id    | int     |
#| student_name  | varchar |
#+---------------+---------+
#student_id is the primary key for this table.
#Each row of this table contains the name and the id of a student in school A.
#
#Table: SchoolB
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| student_id    | int     |
#| student_name  | varchar |
#+---------------+---------+
#student_id is the primary key for this table.
#Each row of this table contains the name and the id of a student in school B.
#
#Table: SchoolC
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| student_id    | int     |
#| student_name  | varchar |
#+---------------+---------+
#student_id is the primary key for this table.
#Each row of this table contains the name and the id of a student in school C.
#
#There is a country with three schools, where each student is enrolled in exactly
#one school. The country is joining a competition and wants to select one student
#from each school to represent the country such that:
#- member_A is selected from SchoolA,
#- member_B is selected from SchoolB,
#- member_C is selected from SchoolC, and
#- The selected students' names and IDs are pairwise distinct (i.e., no two
#  students share the same name, and no two students share the same ID).
#
#Write an SQL query to find all the possible triplets representing the country.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#SchoolA table:
#+------------+--------------+
#| student_id | student_name |
#+------------+--------------+
#| 1          | Alice        |
#| 2          | Bob          |
#+------------+--------------+
#
#SchoolB table:
#+------------+--------------+
#| student_id | student_name |
#+------------+--------------+
#| 3          | Tom          |
#+------------+--------------+
#
#SchoolC table:
#+------------+--------------+
#| student_id | student_name |
#+------------+--------------+
#| 3          | Tom          |
#| 2          | Jerry        |
#| 4          | Alice        |
#+------------+--------------+
#
#Output:
#+----------+----------+----------+
#| member_A | member_B | member_C |
#+----------+----------+----------+
#| Alice    | Tom      | Jerry    |
#| Bob      | Tom      | Alice    |
#+----------+----------+----------+

#SQL Solution:
#SELECT a.student_name AS member_A,
#       b.student_name AS member_B,
#       c.student_name AS member_C
#FROM SchoolA a, SchoolB b, SchoolC c
#WHERE a.student_id != b.student_id
#  AND a.student_id != c.student_id
#  AND b.student_id != c.student_id
#  AND a.student_name != b.student_name
#  AND a.student_name != c.student_name
#  AND b.student_name != c.student_name;

from typing import List, Dict

class Solution:
    def validTriplets(
        self,
        schoolA: List[Dict],
        schoolB: List[Dict],
        schoolC: List[Dict]
    ) -> List[Dict]:
        """
        Python simulation: Find all valid triplets with distinct names and IDs.
        """
        result = []

        for a in schoolA:
            for b in schoolB:
                for c in schoolC:
                    # Check distinct IDs
                    if a['student_id'] == b['student_id']:
                        continue
                    if a['student_id'] == c['student_id']:
                        continue
                    if b['student_id'] == c['student_id']:
                        continue

                    # Check distinct names
                    if a['student_name'] == b['student_name']:
                        continue
                    if a['student_name'] == c['student_name']:
                        continue
                    if b['student_name'] == c['student_name']:
                        continue

                    result.append({
                        'member_A': a['student_name'],
                        'member_B': b['student_name'],
                        'member_C': c['student_name']
                    })

        return result


class SolutionCompact:
    def validTriplets(
        self,
        schoolA: List[Dict],
        schoolB: List[Dict],
        schoolC: List[Dict]
    ) -> List[Dict]:
        """
        Compact solution using set comparisons.
        """
        result = []

        for a in schoolA:
            for b in schoolB:
                for c in schoolC:
                    ids = {a['student_id'], b['student_id'], c['student_id']}
                    names = {a['student_name'], b['student_name'], c['student_name']}

                    if len(ids) == 3 and len(names) == 3:
                        result.append({
                            'member_A': a['student_name'],
                            'member_B': b['student_name'],
                            'member_C': c['student_name']
                        })

        return result
