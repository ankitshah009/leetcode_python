#1355. Activity Participants
#Medium
#
#Table: Friends
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| name          | varchar |
#| activity      | varchar |
#+---------------+---------+
#id is the id of the friend and primary key for this table.
#name is the name of the friend.
#activity is the name of the activity which the friend takes part in.
#
#Table: Activities
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| name          | varchar |
#+---------------+---------+
#id is the primary key for this table.
#name is the name of the activity.
#
#Write an SQL query to find the names of all the activities with neither the
#maximum nor the minimum number of participants.
#
#Each activity in the Activities table is performed by any person in the table
#Friends.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#Friends table:
#+------+--------------+---------------+
#| id   | name         | activity      |
#+------+--------------+---------------+
#| 1    | Jonathan D.  | Eating        |
#| 2    | Jade W.      | Singing       |
#| 3    | Victor J.    | Singing       |
#| 4    | Elvis Q.     | Eating        |
#| 5    | Daniel A.    | Eating        |
#| 6    | Bob B.       | Horse Riding  |
#+------+--------------+---------------+
#Activities table:
#+------+--------------+
#| id   | name         |
#+------+--------------+
#| 1    | Eating       |
#| 2    | Singing      |
#| 3    | Horse Riding |
#+------+--------------+
#Output:
#+-----------+
#| activity  |
#+-----------+
#| Singing   |
#+-----------+
#Explanation:
#Eating activity is performed by 3 friends, maximum number of participants.
#Horse Riding activity is performed by 1 friend, minimum number of participants.
#Singing activity is performed by 2 friends, neither the maximum nor the minimum.

# SQL Solution:
# WITH activity_counts AS (
#     SELECT activity, COUNT(*) AS cnt
#     FROM Friends
#     GROUP BY activity
# )
# SELECT activity
# FROM activity_counts
# WHERE cnt > (SELECT MIN(cnt) FROM activity_counts)
#   AND cnt < (SELECT MAX(cnt) FROM activity_counts);

# Alternative SQL:
# SELECT activity
# FROM Friends
# GROUP BY activity
# HAVING COUNT(*) > (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY COUNT(*) LIMIT 1)
#    AND COUNT(*) < (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY COUNT(*) DESC LIMIT 1);

# Python simulation
from typing import List, Tuple
from collections import Counter

class Solution:
    def activityParticipants(
        self,
        friends: List[Tuple[int, str, str]],
        activities: List[Tuple[int, str]]
    ) -> List[str]:
        """
        Find activities with participant count between min and max.
        """
        # Count participants per activity
        activity_count = Counter(activity for _, _, activity in friends)

        if not activity_count:
            return []

        min_count = min(activity_count.values())
        max_count = max(activity_count.values())

        # Return activities with count strictly between min and max
        return [
            activity for activity, count in activity_count.items()
            if min_count < count < max_count
        ]
