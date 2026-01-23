#1633. Percentage of Users Attended a Contest
#Easy (SQL)
#
#Table: Users
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| user_id     | int     |
#| user_name   | varchar |
#+-------------+---------+
#user_id is the primary key for this table.
#Each row of this table contains the name and the id of a user.
#
#Table: Register
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| contest_id  | int     |
#| user_id     | int     |
#+-------------+---------+
#(contest_id, user_id) is the primary key for this table.
#Each row of this table contains the id of a user and the contest they registered.
#
#Write an SQL query to find the percentage of the users registered in each contest
#rounded to two decimal places.
#
#Return the result table ordered by percentage in descending order. In case of a
#tie, order it by contest_id in ascending order.
#
#Example 1:
#Input:
#Users table:
#+---------+-----------+
#| user_id | user_name |
#+---------+-----------+
#| 6       | Alice     |
#| 2       | Bob       |
#| 7       | Alex      |
#+---------+-----------+
#
#Register table:
#+------------+---------+
#| contest_id | user_id |
#+------------+---------+
#| 215        | 6       |
#| 209        | 2       |
#| 208        | 2       |
#| 210        | 6       |
#| 208        | 6       |
#| 209        | 7       |
#| 209        | 6       |
#| 215        | 7       |
#| 208        | 7       |
#| 210        | 2       |
#| 207        | 2       |
#| 210        | 7       |
#+------------+---------+
#
#Output:
#+------------+------------+
#| contest_id | percentage |
#+------------+------------+
#| 208        | 100.00     |
#| 209        | 100.00     |
#| 210        | 100.00     |
#| 215        | 66.67      |
#| 207        | 33.33      |
#+------------+------------+

#SQL Solution:
#SELECT contest_id,
#       ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
#FROM Register
#GROUP BY contest_id
#ORDER BY percentage DESC, contest_id ASC;

from typing import List, Dict
from collections import Counter

class Solution:
    def contestPercentage(
        self,
        users: List[Dict],
        registers: List[Dict]
    ) -> List[Dict]:
        """
        Python simulation: Calculate percentage of users in each contest.
        """
        total_users = len(users)
        if total_users == 0:
            return []

        # Count users per contest
        contest_users = Counter()
        seen = set()  # (contest_id, user_id) to avoid double counting

        for reg in registers:
            key = (reg['contest_id'], reg['user_id'])
            if key not in seen:
                seen.add(key)
                contest_users[reg['contest_id']] += 1

        # Calculate percentages
        result = []
        for contest_id, count in contest_users.items():
            percentage = round(count * 100.0 / total_users, 2)
            result.append({
                'contest_id': contest_id,
                'percentage': percentage
            })

        # Sort by percentage desc, then contest_id asc
        result.sort(key=lambda x: (-x['percentage'], x['contest_id']))

        return result


class SolutionSet:
    def contestPercentage(
        self,
        users: List[Dict],
        registers: List[Dict]
    ) -> List[Dict]:
        """
        Using sets for unique user counting.
        """
        total = len(users)
        if total == 0:
            return []

        # Group users by contest
        from collections import defaultdict
        contest_to_users = defaultdict(set)

        for reg in registers:
            contest_to_users[reg['contest_id']].add(reg['user_id'])

        result = [
            {
                'contest_id': cid,
                'percentage': round(len(user_set) * 100 / total, 2)
            }
            for cid, user_set in contest_to_users.items()
        ]

        return sorted(result, key=lambda x: (-x['percentage'], x['contest_id']))
