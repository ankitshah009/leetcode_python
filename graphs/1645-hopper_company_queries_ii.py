#1645. Hopper Company Queries II
#Hard (SQL)
#
#Table: Drivers, Rides, AcceptedRides (same schema as 1635)
#
#Write an SQL query to report the percentage of working drivers (active_drivers)
#for each month of 2020 where:
#- A driver is considered active if they accepted at least one ride during that month.
#- The percentage = 100 * (drivers who accepted rides) / (total active drivers)
#
#Return the result table ordered by month in ascending order, where month is
#the month's number.
#
#Example 1:
#(Similar to 1635 with different output format)
#
#Output shows percentage of working drivers per month.

#SQL Solution:
#WITH RECURSIVE months AS (
#    SELECT 1 AS month
#    UNION ALL
#    SELECT month + 1 FROM months WHERE month < 12
#),
#active_drivers AS (
#    SELECT month,
#           (SELECT COUNT(*) FROM Drivers
#            WHERE join_date <= LAST_DAY(CONCAT('2020-', month, '-01'))) as cnt
#    FROM months
#),
#working_drivers AS (
#    SELECT MONTH(r.requested_at) as month,
#           COUNT(DISTINCT a.driver_id) as cnt
#    FROM Rides r
#    JOIN AcceptedRides a ON r.ride_id = a.ride_id
#    WHERE YEAR(r.requested_at) = 2020
#    GROUP BY MONTH(r.requested_at)
#)
#SELECT m.month,
#       IFNULL(ROUND(100 * w.cnt / NULLIF(ad.cnt, 0), 2), 0) AS working_percentage
#FROM months m
#JOIN active_drivers ad ON m.month = ad.month
#LEFT JOIN working_drivers w ON m.month = w.month
#ORDER BY m.month;

from typing import List, Dict

class Solution:
    def hopperQueriesII(
        self,
        drivers: List[Dict],
        rides: List[Dict],
        accepted_rides: List[Dict]
    ) -> List[Dict]:
        """
        Calculate percentage of working drivers per month in 2020.
        """
        # Build ride_id -> driver_id mapping for accepted rides
        ride_to_driver = {ar['ride_id']: ar['driver_id'] for ar in accepted_rides}

        # Count drivers before 2020 and during each month
        drivers_before_2020 = 0
        drivers_in_month = [0] * 13

        for d in drivers:
            join_date = d['join_date']
            if isinstance(join_date, str):
                year, month = int(join_date[:4]), int(join_date[5:7])
            else:
                year, month = join_date.year, join_date.month

            if year < 2020:
                drivers_before_2020 += 1
            elif year == 2020:
                drivers_in_month[month] += 1

        # Cumulative active drivers
        active = [0] * 13
        active[0] = drivers_before_2020
        for m in range(1, 13):
            active[m] = active[m - 1] + drivers_in_month[m]

        # Count unique working drivers per month
        working_per_month = [set() for _ in range(13)]

        for ride in rides:
            if ride['ride_id'] in ride_to_driver:
                req_date = ride['requested_at']
                if isinstance(req_date, str):
                    year, month = int(req_date[:4]), int(req_date[5:7])
                else:
                    year, month = req_date.year, req_date.month

                if year == 2020:
                    driver_id = ride_to_driver[ride['ride_id']]
                    working_per_month[month].add(driver_id)

        # Calculate percentage
        result = []
        for month in range(1, 13):
            total = active[month]
            working = len(working_per_month[month])

            if total == 0:
                percentage = 0.0
            else:
                percentage = round(100 * working / total, 2)

            result.append({
                'month': month,
                'working_percentage': percentage
            })

        return result
