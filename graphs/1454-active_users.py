#1454. Active Users
#Medium
#
#Table: Accounts
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| name          | varchar |
#+---------------+---------+
#id is the primary key for this table.
#
#Table: Logins
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| login_date    | date    |
#+---------------+---------+
#There is no primary key for this table, it may contain duplicates.
#
#Active users are those who logged in to their accounts for five or more
#consecutive days.
#
#Write an SQL query to find the id and the name of active users.
#
#Return the result table ordered by id.
#
#Example 1:
#Input:
#Accounts table:
#+----+----------+
#| id | name     |
#+----+----------+
#| 1  | Winston  |
#| 7  | Jonathan |
#+----+----------+
#Logins table:
#+----+------------+
#| id | login_date |
#+----+------------+
#| 7  | 2020-05-30 |
#| 1  | 2020-05-30 |
#| 7  | 2020-05-31 |
#| 7  | 2020-06-01 |
#| 7  | 2020-06-02 |
#| 7  | 2020-06-02 |
#| 7  | 2020-06-03 |
#| 1  | 2020-06-07 |
#| 7  | 2020-06-10 |
#+----+------------+
#Output:
#+----+----------+
#| id | name     |
#+----+----------+
#| 7  | Jonathan |
#+----+----------+
#Explanation:
#User Winston with id = 1 logged in 2 times only in 2 different days, so,
#Winston is not an active user.
#User Jonathan with id = 7 logged in 7 times in 6 different days, five of them
#were consecutive days, so, Jonathan is an active user.

#SQL Solution using self-join:
#SELECT DISTINCT a.id, a.name
#FROM Accounts a
#WHERE a.id IN (
#    SELECT DISTINCT l1.id
#    FROM Logins l1
#    JOIN Logins l2 ON l1.id = l2.id AND DATEDIFF(l2.login_date, l1.login_date) BETWEEN 1 AND 4
#    GROUP BY l1.id, l1.login_date
#    HAVING COUNT(DISTINCT l2.login_date) = 4
#)
#ORDER BY a.id;

#Alternative SQL using window functions:
#WITH consecutive AS (
#    SELECT
#        id,
#        login_date,
#        ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date) -
#        DATEDIFF(login_date, '2000-01-01') AS grp
#    FROM (SELECT DISTINCT id, login_date FROM Logins) t
#)
#SELECT DISTINCT a.id, a.name
#FROM consecutive c
#JOIN Accounts a ON c.id = a.id
#GROUP BY c.id, c.grp
#HAVING COUNT(*) >= 5
#ORDER BY a.id;

from typing import List
from collections import defaultdict
from datetime import timedelta

class Solution:
    def activeUsers(self, accounts: List[dict], logins: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Find users with 5+ consecutive login days.
        """
        # Get unique login dates per user
        user_dates = defaultdict(set)
        for login in logins:
            user_dates[login['id']].add(login['login_date'])

        # Build account names map
        account_names = {a['id']: a['name'] for a in accounts}

        active_ids = set()

        for user_id, dates in user_dates.items():
            # Sort dates
            sorted_dates = sorted(dates)

            # Find consecutive runs
            consecutive = 1
            for i in range(1, len(sorted_dates)):
                if (sorted_dates[i] - sorted_dates[i-1]).days == 1:
                    consecutive += 1
                    if consecutive >= 5:
                        active_ids.add(user_id)
                        break
                else:
                    consecutive = 1

        # Build result
        result = [
            {'id': uid, 'name': account_names[uid]}
            for uid in sorted(active_ids)
        ]

        return result


class SolutionExplicit:
    def activeUsers(self, accounts: List[dict], logins: List[dict]) -> List[dict]:
        """More explicit consecutive day checking"""
        # Group logins by user
        user_logins = defaultdict(list)
        for login in logins:
            user_logins[login['id']].append(login['login_date'])

        account_names = {a['id']: a['name'] for a in accounts}

        active_users = []

        for user_id, dates in user_logins.items():
            # Remove duplicates and sort
            unique_dates = sorted(set(dates))

            # Check for 5 consecutive days
            max_consecutive = 1
            current_consecutive = 1

            for i in range(1, len(unique_dates)):
                if (unique_dates[i] - unique_dates[i-1]).days == 1:
                    current_consecutive += 1
                    max_consecutive = max(max_consecutive, current_consecutive)
                else:
                    current_consecutive = 1

            if max_consecutive >= 5:
                active_users.append({
                    'id': user_id,
                    'name': account_names[user_id]
                })

        # Sort by id
        active_users.sort(key=lambda x: x['id'])
        return active_users
