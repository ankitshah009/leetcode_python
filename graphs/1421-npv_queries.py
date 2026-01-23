#1421. NPV Queries
#Easy
#
#Table: NPV
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| year          | int     |
#| npv           | int     |
#+---------------+---------+
#(id, year) is the primary key of this table.
#The table has information about the id and the year of each inventory and
#the corresponding net present value.
#
#Table: Queries
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| year          | int     |
#+---------------+---------+
#(id, year) is the primary key of this table.
#The table has information about the id and the year of each inventory query.
#
#Write an SQL query to find the npv of each query. If the corresponding query
#does not have an entry in the NPV table, the answer is 0.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#NPV table:
#+------+--------+--------+
#| id   | year   | npv    |
#+------+--------+--------+
#| 1    | 2018   | 100    |
#| 7    | 2020   | 30     |
#| 13   | 2019   | 40     |
#| 1    | 2019   | 113    |
#| 2    | 2008   | 121    |
#| 3    | 2009   | 12     |
#| 11   | 2020   | 99     |
#| 7    | 2019   | 0      |
#+------+--------+--------+
#Queries table:
#+------+--------+
#| id   | year   |
#+------+--------+
#| 1    | 2019   |
#| 2    | 2008   |
#| 3    | 2009   |
#| 7    | 2018   |
#| 7    | 2019   |
#| 7    | 2020   |
#| 13   | 2019   |
#+------+--------+
#Output:
#+------+--------+--------+
#| id   | year   | npv    |
#+------+--------+--------+
#| 1    | 2019   | 113    |
#| 2    | 2008   | 121    |
#| 3    | 2009   | 12     |
#| 7    | 2018   | 0      |
#| 7    | 2019   | 0      |
#| 7    | 2020   | 30     |
#| 13   | 2019   | 40     |
#+------+--------+--------+

#SQL Solution:
#SELECT q.id, q.year, COALESCE(n.npv, 0) as npv
#FROM Queries q
#LEFT JOIN NPV n ON q.id = n.id AND q.year = n.year;

from typing import List

class Solution:
    def npvQueries(self, npv: List[dict], queries: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Left join queries with NPV on (id, year).
        """
        # Create lookup from NPV table
        npv_lookup = {}
        for row in npv:
            key = (row['id'], row['year'])
            npv_lookup[key] = row['npv']

        # Process queries
        result = []
        for query in queries:
            key = (query['id'], query['year'])
            value = npv_lookup.get(key, 0)
            result.append({
                'id': query['id'],
                'year': query['year'],
                'npv': value
            })

        return result


class SolutionExplicit:
    def npvQueries(self, npv: List[dict], queries: List[dict]) -> List[dict]:
        """More explicit version"""
        # Build NPV dictionary
        npv_dict = {}
        for entry in npv:
            npv_dict[(entry['id'], entry['year'])] = entry['npv']

        # Answer queries
        answers = []
        for q in queries:
            lookup_key = (q['id'], q['year'])
            npv_value = npv_dict.get(lookup_key, 0)

            answers.append({
                'id': q['id'],
                'year': q['year'],
                'npv': npv_value
            })

        return answers
