#1635. Hopper Company Queries I
#Hard (SQL)
#
#Table: Drivers
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| driver_id   | int     |
#| join_date   | date    |
#+-------------+---------+
#driver_id is the primary key for this table.
#Each row of this table contains the driver's ID and the date they joined.
#
#Table: Rides
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| ride_id     | int     |
#| user_id     | int     |
#| requested_at| date    |
#+-------------+---------+
#ride_id is the primary key for this table.
#Each row of this table contains the ID of a ride, the user's ID that requested
#it, and the date it was requested.
#
#Table: AcceptedRides
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| ride_id       | int     |
#| driver_id     | int     |
#| ride_distance | int     |
#| ride_duration | int     |
#+---------------+---------+
#ride_id is the primary key for this table.
#Each row of this table contains some information about an accepted ride.
#
#Write an SQL query to report the following statistics for each month of 2020:
#- The number of drivers currently with the Hopper company by the end of the
#  month (active_drivers).
#- The number of accepted rides in that month (accepted_rides).
#
#Return the result table ordered by month in ascending order, where month is
#the month's number (January is 1, February is 2, etc.).
#
#Example 1:
#Input:
#Drivers table:
#+-----------+------------+
#| driver_id | join_date  |
#+-----------+------------+
#| 10        | 2019-12-10 |
#| 8         | 2020-01-13 |
#| 5         | 2020-02-16 |
#| 7         | 2020-03-08 |
#| 4         | 2020-05-17 |
#| 1         | 2020-10-24 |
#| 6         | 2021-01-05 |
#+-----------+------------+
#
#Rides table:
#+---------+---------+--------------+
#| ride_id | user_id | requested_at |
#+---------+---------+--------------+
#| 6       | 75      | 2019-12-09   |
#| 1       | 54      | 2020-02-09   |
#| 10      | 63      | 2020-03-04   |
#| 19      | 39      | 2020-04-06   |
#| 3       | 41      | 2020-06-03   |
#| 13      | 52      | 2020-06-22   |
#| 7       | 69      | 2020-07-16   |
#| 17      | 70      | 2020-08-25   |
#| 20      | 81      | 2020-11-02   |
#| 5       | 57      | 2020-11-09   |
#| 2       | 42      | 2020-12-09   |
#| 11      | 68      | 2021-01-11   |
#| 15      | 32      | 2021-01-17   |
#| 12      | 11      | 2021-01-19   |
#| 14      | 18      | 2021-01-27   |
#+---------+---------+--------------+
#
#AcceptedRides table:
#+---------+-----------+---------------+---------------+
#| ride_id | driver_id | ride_distance | ride_duration |
#+---------+-----------+---------------+---------------+
#| 10      | 10        | 63            | 38            |
#| 13      | 10        | 73            | 96            |
#| 7       | 8         | 100           | 28            |
#| 17      | 7         | 119           | 68            |
#| 20      | 1         | 121           | 92            |
#| 5       | 7         | 42            | 101           |
#| 2       | 4         | 6             | 38            |
#| 11      | 8         | 37            | 43            |
#| 15      | 8         | 108           | 82            |
#| 12      | 8         | 38            | 34            |
#| 14      | 1         | 90            | 74            |
#+---------+-----------+---------------+---------------+
#
#Output:
#+-------+----------------+----------------+
#| month | active_drivers | accepted_rides |
#+-------+----------------+----------------+
#| 1     | 2              | 0              |
#| 2     | 3              | 0              |
#| 3     | 4              | 1              |
#| 4     | 4              | 0              |
#| 5     | 5              | 0              |
#| 6     | 5              | 1              |
#| 7     | 5              | 1              |
#| 8     | 5              | 1              |
#| 9     | 5              | 0              |
#| 10    | 6              | 0              |
#| 11    | 6              | 2              |
#| 12    | 6              | 1              |
#+-------+----------------+----------------+

#SQL Solution (using recursive CTE for months):
#WITH RECURSIVE months AS (
#    SELECT 1 AS month
#    UNION ALL
#    SELECT month + 1 FROM months WHERE month < 12
#),
#active AS (
#    SELECT month,
#           (SELECT COUNT(*) FROM Drivers WHERE join_date <= LAST_DAY(CONCAT('2020-', month, '-01'))) AS active_drivers
#    FROM months
#),
#rides_2020 AS (
#    SELECT MONTH(r.requested_at) AS month, COUNT(*) AS accepted_rides
#    FROM Rides r
#    JOIN AcceptedRides a ON r.ride_id = a.ride_id
#    WHERE YEAR(r.requested_at) = 2020
#    GROUP BY MONTH(r.requested_at)
#)
#SELECT m.month, a.active_drivers, COALESCE(r.accepted_rides, 0) AS accepted_rides
#FROM months m
#JOIN active a ON m.month = a.month
#LEFT JOIN rides_2020 r ON m.month = r.month
#ORDER BY m.month;

from typing import List, Dict
from collections import defaultdict
from datetime import date

class Solution:
    def hopperQueries(
        self,
        drivers: List[Dict],
        rides: List[Dict],
        accepted_rides: List[Dict]
    ) -> List[Dict]:
        """
        Python simulation: Calculate active drivers and accepted rides per month in 2020.
        """
        # Build accepted ride lookup
        accepted_ride_ids = {ar['ride_id'] for ar in accepted_rides}

        # Count drivers before 2020 and during each month of 2020
        drivers_before_2020 = 0
        drivers_per_month = [0] * 13  # Index 1-12

        for d in drivers:
            join_date = d['join_date']
            if isinstance(join_date, str):
                year, month, day = map(int, join_date.split('-'))
            else:
                year, month = join_date.year, join_date.month

            if year < 2020:
                drivers_before_2020 += 1
            elif year == 2020:
                drivers_per_month[month] += 1

        # Calculate cumulative active drivers
        active = [0] * 13
        active[0] = drivers_before_2020
        for m in range(1, 13):
            active[m] = active[m - 1] + drivers_per_month[m]

        # Count accepted rides per month in 2020
        accepted_per_month = [0] * 13

        for ride in rides:
            if ride['ride_id'] in accepted_ride_ids:
                req_date = ride['requested_at']
                if isinstance(req_date, str):
                    year, month, day = map(int, req_date.split('-'))
                else:
                    year, month = req_date.year, req_date.month

                if year == 2020:
                    accepted_per_month[month] += 1

        # Build result
        result = []
        for month in range(1, 13):
            result.append({
                'month': month,
                'active_drivers': active[month],
                'accepted_rides': accepted_per_month[month]
            })

        return result
