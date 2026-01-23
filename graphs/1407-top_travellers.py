#1407. Top Travellers
#Easy
#
#Table: Users
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| name          | varchar |
#+---------------+---------+
#id is the primary key for this table.
#
#Table: Rides
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| user_id       | int     |
#| distance      | int     |
#+---------------+---------+
#id is the primary key for this table.
#user_id is the id of the user who traveled the distance in this ride.
#
#Write an SQL query to report the distance traveled by each user.
#Return the result table ordered by travelled_distance in descending order, if
#two or more users traveled the same distance, order them by their name in
#ascending order.
#
#Example 1:
#Input:
#Users table:
#+------+-----------+
#| id   | name      |
#+------+-----------+
#| 1    | Alice     |
#| 2    | Bob       |
#| 3    | Alex      |
#| 4    | Donald    |
#| 7    | Lee       |
#| 13   | Jonathan  |
#| 19   | Elvis     |
#+------+-----------+
#Rides table:
#+------+----------+----------+
#| id   | user_id  | distance |
#+------+----------+----------+
#| 1    | 1        | 120      |
#| 2    | 2        | 317      |
#| 3    | 3        | 222      |
#| 4    | 7        | 100      |
#| 5    | 13       | 312      |
#| 6    | 19       | 50       |
#| 7    | 7        | 120      |
#| 8    | 19       | 400      |
#| 9    | 7        | 230      |
#+------+----------+----------+
#Output:
#+----------+--------------------+
#| name     | travelled_distance |
#+----------+--------------------+
#| Elvis    | 450                |
#| Lee      | 450                |
#| Bob      | 317                |
#| Jonathan | 312                |
#| Alex     | 222                |
#| Alice    | 120                |
#| Donald   | 0                  |
#+----------+--------------------+

#SQL Solution:
#SELECT u.name, COALESCE(SUM(r.distance), 0) as travelled_distance
#FROM Users u
#LEFT JOIN Rides r ON u.id = r.user_id
#GROUP BY u.id, u.name
#ORDER BY travelled_distance DESC, u.name ASC;

from typing import List
from collections import defaultdict

class Solution:
    def topTravellers(self, users: List[dict], rides: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Calculate total distance for each user.
        """
        # Calculate total distance per user
        distances = defaultdict(int)
        for ride in rides:
            distances[ride['user_id']] += ride['distance']

        # Build result with all users
        result = []
        for user in users:
            result.append({
                'name': user['name'],
                'travelled_distance': distances.get(user['id'], 0)
            })

        # Sort by distance descending, then name ascending
        result.sort(key=lambda x: (-x['travelled_distance'], x['name']))

        return result


class SolutionExplicit:
    def topTravellers(self, users: List[dict], rides: List[dict]) -> List[dict]:
        """More explicit version"""
        # Map user_id to name
        user_names = {u['id']: u['name'] for u in users}

        # Calculate total distance
        total_distance = {user_id: 0 for user_id in user_names}
        for ride in rides:
            user_id = ride['user_id']
            if user_id in total_distance:
                total_distance[user_id] += ride['distance']

        # Build result
        result = [
            {'name': user_names[uid], 'travelled_distance': dist}
            for uid, dist in total_distance.items()
        ]

        # Sort
        result.sort(key=lambda x: (-x['travelled_distance'], x['name']))

        return result
