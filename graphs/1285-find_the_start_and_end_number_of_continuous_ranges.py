#1285. Find the Start and End Number of Continuous Ranges
#Medium
#
#Table: Logs
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| log_id        | int     |
#+---------------+---------+
#log_id is the primary key for this table.
#Each row of this table contains the ID in a log Table.
#
#Write an SQL query to find the start and end number of continuous ranges in
#the table Logs.
#
#Return the result table ordered by start_id.
#
#Example 1:
#Input:
#Logs table:
#+------------+
#| log_id     |
#+------------+
#| 1          |
#| 2          |
#| 3          |
#| 7          |
#| 8          |
#| 10         |
#+------------+
#Output:
#+------------+--------------+
#| start_id   | end_id       |
#+------------+--------------+
#| 1          | 3            |
#| 7          | 8            |
#| 10         | 10           |
#+------------+--------------+

# SQL Solution:
# SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
# FROM (
#     SELECT log_id, log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
#     FROM Logs
# ) t
# GROUP BY grp
# ORDER BY start_id;

# Python simulation for the algorithm
from typing import List, Tuple

class Solution:
    def findContinuousRanges(self, logs: List[int]) -> List[Tuple[int, int]]:
        """
        Find continuous ranges in sorted log IDs.
        Uses the difference between value and index to group consecutive numbers.
        """
        if not logs:
            return []

        logs = sorted(logs)
        result = []
        start = logs[0]

        for i in range(1, len(logs)):
            # If not consecutive, end current range and start new
            if logs[i] != logs[i - 1] + 1:
                result.append((start, logs[i - 1]))
                start = logs[i]

        # Don't forget last range
        result.append((start, logs[-1]))

        return result


class SolutionGroupBy:
    def findContinuousRanges(self, logs: List[int]) -> List[Tuple[int, int]]:
        """Using the row_number grouping technique"""
        if not logs:
            return []

        logs = sorted(logs)
        from collections import defaultdict

        # Group by (value - index) which is constant for consecutive numbers
        groups = defaultdict(list)
        for i, val in enumerate(logs):
            groups[val - i].append(val)

        result = []
        for group in groups.values():
            result.append((min(group), max(group)))

        return sorted(result)
