#1435. Create a Session Bar Chart
#Easy
#
#Table: Sessions
#+---------------------+---------+
#| Column Name         | Type    |
#+---------------------+---------+
#| session_id          | int     |
#| duration            | int     |
#+---------------------+---------+
#session_id is the primary key for this table.
#duration is the time in seconds that a user has visited the application.
#
#You want to know how long a user visits your application. You decided to create
#bins of "[0-5>", "[5-10>", "[10-15>", and "15 minutes or more" and count the
#number of sessions on it.
#
#Write an SQL query to report the (bin, total).
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Sessions table:
#+-------------+---------------+
#| session_id  | duration      |
#+-------------+---------------+
#| 1           | 30            |
#| 2           | 199           |
#| 3           | 299           |
#| 4           | 580           |
#| 5           | 1000          |
#+-------------+---------------+
#Output:
#+-------------+--------------+
#| bin         | total        |
#+-------------+--------------+
#| [0-5>       | 3            |
#| [5-10>      | 1            |
#| [10-15>     | 0            |
#| 15 or more  | 1            |
#+-------------+--------------+
#Explanation:
#For session_id 1, 2, and 3 have a duration greater or equal than 0 minutes and
#less than 5 minutes.
#For session_id 4 has a duration greater or equal than 5 minutes and less than
#10 minutes.
#There is no session with a duration greater than or equal to 10 minutes and
#less than 15 minutes.
#For session_id 5 has a duration greater than or equal to 15 minutes.

#SQL Solution:
#SELECT '[0-5>' AS bin, COUNT(*) AS total
#FROM Sessions WHERE duration >= 0 AND duration < 300
#UNION ALL
#SELECT '[5-10>' AS bin, COUNT(*) AS total
#FROM Sessions WHERE duration >= 300 AND duration < 600
#UNION ALL
#SELECT '[10-15>' AS bin, COUNT(*) AS total
#FROM Sessions WHERE duration >= 600 AND duration < 900
#UNION ALL
#SELECT '15 or more' AS bin, COUNT(*) AS total
#FROM Sessions WHERE duration >= 900;

#Alternative SQL using CASE:
#SELECT
#    bin,
#    COUNT(session_id) AS total
#FROM (
#    SELECT
#        session_id,
#        CASE
#            WHEN duration < 300 THEN '[0-5>'
#            WHEN duration < 600 THEN '[5-10>'
#            WHEN duration < 900 THEN '[10-15>'
#            ELSE '15 or more'
#        END AS bin
#    FROM Sessions
#) t
#RIGHT JOIN (
#    SELECT '[0-5>' AS bin
#    UNION SELECT '[5-10>'
#    UNION SELECT '[10-15>'
#    UNION SELECT '15 or more'
#) bins ON t.bin = bins.bin
#GROUP BY bins.bin;

from typing import List

class Solution:
    def createSessionBarChart(self, sessions: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Categorize sessions into time bins.
        """
        bins = {
            '[0-5>': 0,
            '[5-10>': 0,
            '[10-15>': 0,
            '15 or more': 0
        }

        for session in sessions:
            duration = session['duration']

            if duration < 300:
                bins['[0-5>'] += 1
            elif duration < 600:
                bins['[5-10>'] += 1
            elif duration < 900:
                bins['[10-15>'] += 1
            else:
                bins['15 or more'] += 1

        return [{'bin': bin_name, 'total': count}
                for bin_name, count in bins.items()]


class SolutionExplicit:
    def createSessionBarChart(self, sessions: List[dict]) -> List[dict]:
        """More explicit version"""
        def get_bin(duration: int) -> str:
            if duration < 300:  # < 5 minutes
                return '[0-5>'
            elif duration < 600:  # < 10 minutes
                return '[5-10>'
            elif duration < 900:  # < 15 minutes
                return '[10-15>'
            else:
                return '15 or more'

        # Initialize all bins with 0
        counts = {
            '[0-5>': 0,
            '[5-10>': 0,
            '[10-15>': 0,
            '15 or more': 0
        }

        # Count sessions in each bin
        for session in sessions:
            bin_name = get_bin(session['duration'])
            counts[bin_name] += 1

        # Format result
        return [{'bin': b, 'total': c} for b, c in counts.items()]
